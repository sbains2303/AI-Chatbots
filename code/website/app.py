from flask import Flask, render_template
import yaml

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template("layout.html")

with open("templates/scrambled-eggs-content.yaml", "r") as file:
    scrambled_eggs_content = yaml.safe_load(file)

@app.route('/scrambled-eggs')
def scrambledEggs():
    return render_template("recipes.html", **scrambled_eggs_content)

with open("templates/chicken-korma.yaml", "r") as file:
    chicken_korma_content = yaml.safe_load(file)

@app.route('/chicken-korma')
def chickenKorma():
    return render_template("recipes.html", **chicken_korma_content)

with open("templates/salmon-fishcakes-content.yaml", "r") as file:
    salmon_fishcakes_content = yaml.safe_load(file)

@app.route('/salmon-fishcakes')
def salmonFishcakes():
    return render_template("recipes.html", **salmon_fishcakes_content)

@app.route('/new-recipe')
def newRecipe():
    return render_template("new-recipe.html")