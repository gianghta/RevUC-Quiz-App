from flask import Flask, render_template
import random
from random_quiz import generate_test, get_question, change_to_html

app = Flask(__name__)

@app.route('/')
def index():
    number = random.randint(0, 2)

    # Get question data
    question = get_question("questions.txt", number)

    # Split question data into variables to add to 4 answer buttons
    # Question data format: [country], [correct_answer]*[choice1], [chioce2], [choice3], [choice4],
    splitted = question.split("*")
    country, correct_city = splitted[0].split(",")
    choices = splitted[1].strip().split(",")[0:-1]
    

    # Display question and 4 answer choice   
    return render_template('index.html', country = country, choices = choices)


@app.route('/play')
def play_page():
    return render_template('play.html')

if __name__ == "__main__":
    app.run(debug=True)