from datetime import datetime
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

current_time_month = datetime.now().strftime("%B")
current_time_day = datetime.now().day
current_time_year = datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", month = current_time_month, day=current_time_day, year=current_time_year)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/myhobbyprojects')
def hobbies():
    return render_template('hobbies.html')

@app.route('/myfutureprojects')
def futureprojects():
    return render_template('futureprojects.html')

if __name__ == "__main__":
    app.run(debug=True)

