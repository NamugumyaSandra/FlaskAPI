from flask import Flask, jsonify, request, Response

app = Flask(__name__)

questions = [
    {
        'questionId': 1, 
        'question': 'How can I use the flex option in HTML inplace of a table?', 
        'answer': 'There are two options when one uses flex, either use flex-direction row or column depending on requirements.'
    },

    {
        'questionId': 2, 
        'question': 'How do I set my email address to a specific format in python?', 
        'answer': 'You can use regular expressions in python - REGEX.'
    }
]


@app.route('/app/v1/questions', methods=['GET'])
def get_questions():
    response = Response('', 200, mimetype='application/json')
    response.headers['Location'] = 'questions/'
    return jsonify(questions), 200

@app.route('/app/v1/questions', methods=['POST'])
def add_question():
    questions.append(request.get_json())
    response = Response('', 201,mimetype="application/json")
    response.headers['Location'] = 'questions/'+ str(request.json['questionId'])
    return jsonify(questions),201

@app.route('/app/v1/questions/<int:questionId>', methods=['GET'])
def get_a_question(questionId):
    qn = [question for question in questions if question['questionId']==questionId]
    response = Response('', 200, mimetype='application/json')
    response.headers['Location'] = '<int:questionId>/'+ str(request.json['questionId'])
    return jsonify({'question': qn[0]}), 200

@app.route('/app/v1/questions/<int:questionId>/answers', methods=['POST'])
def add_answer(questionId):
    qn = [question for question in questions if question['questionId']==questionId]
    qn.append(request.get_json())
    response = Response('', 201, mimetype='application/json')
    response.headers['Location'] = 'answers/'+ str(request.json['questionId'])
    return jsonify({'question': qn[1]})
  
if __name__ == '__main__':
    app.run(debug=True, port=5000)

