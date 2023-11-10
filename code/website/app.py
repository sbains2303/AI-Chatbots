from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chicken-korma')
def chickenKorma():
    return render_template("chicken-korma.html")
