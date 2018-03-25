# Flask interface setup

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index.htm')
def index():
    return render_template("index.htm")

@app.route('/individual.htm')
def individual():
    return render_template("individual.htm")

@app.route('/group.htm')
def group():
    return render_template("group.htm")

@app.route('/blaster.htm')
def blaster():
    return render_template("blaster.htm")

@app.route('/pattern.htm')
def pattern():
    return render_template("pattern.htm")


