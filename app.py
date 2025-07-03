from flask import Flask, render_template, request

app = Flask(__name__)

# Quiz data
quizzes = {
    'science': [
        {"q": "What planet is called the Red Planet?", "options": ["Earth", "Mars", "Venus"], "answer": "Mars"},
        {"q": "What is H2O?", "options": ["Water", "Oxygen", "Hydrogen"], "answer": "Water"}
    ],
    'math': [
        {"q": "2 + 2 = ?", "options": ["3", "4", "5"], "answer": "4"},
        {"q": "10 ÷ 2 = ?", "options": ["3", "5", "10"], "answer": "5"}
    ]
}

@app.route('/')
def home():
    return render_template('home.html', topics=quizzes.keys())

@app.route('/quiz/<topic>', methods=['GET', 'POST'])
def quiz(topic):
    questions = quizzes.get(topic, [])
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(questions):
            selected = request.form.get(f'q{i}')
            if selected == q["answer"]:
                score += 1
        return render_template('result.html', score=score, total=len(questions))
    return render_template('quiz.html', topic=topic, questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
