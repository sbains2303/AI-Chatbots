from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chicken-korma')
def chickenKorma():
    return render_template("chicken-korma.html")

@app.route('/scrambled-eggs')
def scrambledEggs():
    return render_template("scrambled-eggs.html")

@app.route('/salmon-fishcakes')
def salmonFishcakes():
    return render_template("salmon-fishcakes.html")

