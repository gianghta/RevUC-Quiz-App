from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
import random
from cs50 import SQL

from random_quiz import generate_test, get_question, shuffle_question_order

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

capitals = generate_test("nations-and-capitals.txt", "questions.txt", 4)

db = SQL("sqlite:///userbase.db")

def get_scores_numpassed(username, password):
    rows = db.execute("SELECT score, num_passed FROM userbase WHERE username = ? AND password = ?",
                      username, password)
    only_row = rows[0]
    return only_row["score"], only_row["num_passed"]

def update_score(username, score):
    db.execute("UPDATE userbase SET score = ? WHERE username = ?", score, username)

def update_numpassed(username, num_passed):
    db.execute("UPDATE userbase SET num_passed = ? WHERE username = ?", num_passed, username)

def new_acc(username, password):
    db.execute("INSERT INTO userbase (username, password, score, num_passed) VALUES (?, ?, 0, 0)", username, password)

username = ""
password = ""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        global username
        global password
        username = ""
        password = ""
        user = request.form.get("username")
        pw = request.form.get("password")
        row = db.execute("SELECT * FROM userbase WHERE username = ? AND password = ?", user, pw)
        if len(row) == 1:
            if "num_passed" not in session:
                session["num_passed"] = get_scores_numpassed(user, pw)[1]
            if "order" not in session:
                session["order"] = shuffle_question_order("questions.txt")
            if "score" not in session:
                session["score"] = get_scores_numpassed(user, pw)[0] 
            
            username = user
            password = pw           
            return redirect("/play")
        else:
            return redirect("/login")


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        user_new = request.form.get("username")
        pw_new = request.form.get("password")
        new_acc(user_new, pw_new)
        if "num_passed" not in session:
            session["num_passed"] = 0
        if "order" not in session:
            session["order"] = shuffle_question_order("questions.txt")
        if "score" not in session:
            session["score"] = 0
        update_numpassed(user_new, session['num_passed'])
        update_score(user_new, session["score"])
        return redirect("/login")


@app.route('/play')
def play():    
    if "num_passed" not in session:
        session["num_passed"] = 0
    if "order" not in session:
        session["order"] = shuffle_question_order("questions.txt")
    if "score" not in session:
        session["score"] = 0

    if session["num_passed"] >= len(capitals):
        return redirect("/endgame")
    else:
        
        # Get question data
        question_index = session["order"][session["num_passed"]]
        question = get_question("questions.txt", question_index)

        # Split question data into variables to add to 4 answer buttons
        # Question data format: [country], [correct_answer]*[choice1], [chioce2], [choice3], [choice4],
        splitted = question.split("*")
        country, correct_city = splitted[0].split(",")
        choices = splitted[1].strip().split(",")[0:-1]

        
        cor = request.args.get("cor")
        country_previous = request.args.get("country")
        
        if cor and country_previous:
            result_ans = ""
            result_ans = "CORRECT" if cor == "true" else "WRONG"
            return render_template('play.html', 
                                    country = country_previous, 
                                    choices = choices, 
                                    score = session["score"],
                                    result = result_ans,
                                    input_disabled="true")
        
        else:
        # Display question and 4 answer choice  
            
            return render_template('play.html', 
                                country = country, 
                                choices = choices, 
                                score = session["score"],
                                result = "",
                                input_disabled="false")
    return render_template('index.html')

    


@app.route('/check', methods=["GET", "POST"])
def check():
    if request.method == "POST":
        choice_and_country = request.form.get("choice")
        choice, country = choice_and_country.split(",")
    
        if choice == capitals[country]:
            session["score"] += 100
            update_score(username, session["score"])
            return redirect(f"/play?cor=true&country={country}")
        else:
            return redirect(f"/play?cor=false&country={country}")


@app.route("/next")
def next():
    session["num_passed"] += 1
    update_numpassed(username, session['num_passed'])
    if session["num_passed"] >= len(capitals):
        return redirect("/endgame")
    else:
        return redirect("/play")


@app.route("/endgame", methods = ["GET", "POST"])
def endgame():
    score = session['score']
    if request.method == "GET":
        return render_template("endgame.html", score=score)
    else:
        reset = request.form.get("reset")
        if reset == "reset":
            session.clear()
            if "num_passed" not in session:
                session["num_passed"] = 0
            if "order" not in session:
                session["order"] = shuffle_question_order("questions.txt")
            if "score" not in session:
                session["score"] = 0
            update_numpassed(username, session['num_passed'])
            update_score(username, session["score"])
            return redirect("./play")
        
        logout = request.form.get('logout')
        if logout == "logout":
            session.clear()
            return redirect("./login")



if __name__ == "__main__":
    app.run(debug=True, TEMPLATES_AUTO_RELOAD=True)