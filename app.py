from flask import Flask, render_template
import random
from random_quiz import generate_test, get_question, change_to_html

app = Flask(__name__)

@app.route('/')
def index():
    number = random.randint(0, 2)
    question = get_question("questions.txt", number)
    question_html = change_to_html(question)
    return render_template('index.html', question = question_html)


@app.route('/play')
def test_page():
    return render_template('play.html')

if __name__ == "__main__":
    app.run(debug=True)