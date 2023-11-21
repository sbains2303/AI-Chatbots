from flask import Flask, render_template, request, g
# import sqlite3

import sqlalchemy

app = Flask(__name__, static_url_path='/static')
db = sqlalchemy(app)

app.config['DATABASE'] = 'cookbook.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cookbook.db'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipe/<recipe_name>')
def serveRecipe(recipe_name):
    
    return render_template("build_recipe.html")


@app.route('/publish', methods=['POST'])
def publish():
    author_name = request.form['authorname']
    email = request.form['email']
    recipe_name = request.form['recipename']
    recipe_desc = request.form['recipedesc']
    serves = request.form['serves']
    image = request.form['image']
    time = request.form['time']
    ingredients = eval(request.form['ingredients'])  # Assuming the ingredients are a list of pairs
    steps = eval(request.form['steps'])  # Assuming the steps are a list
    cuisine_name = request.form['cuisine']

    # Check if the cuisine exists, if not, add it
    cuisine = db.Cuisine.query.filter_by(cuisine_name=cuisine_name).first()
    if not cuisine:
        cuisine = db.Cuisine(cuisine_name=cuisine_name)
        db.session.add(cuisine)
        db.session.commit()

    # Check if the author exists, if not, add them
    author = db.Author.query.filter_by(name=author_name).first()
    if not author:
        author = db.Author(name=author_name, email=email)
        db.session.add(author)
        db.session.commit()

    # Create the recipe
    recipe = db.Recipe(
        name=recipe_name,
        description=recipe_desc,
        cuisine=cuisine,
        serves=serves,
        image=image,
        cooking_time=time,
        author=author
    )
    db.session.add(recipe)
    db.session.commit()

    # Add ingredients to the recipe
    for ingredient in ingredients:
        ingredient_obj = db.Ingredient(recipe=recipe, name=ingredient[0], quantity=ingredient[1])
        db.session.add(ingredient_obj)

    # Add steps to the recipe
    for i, step in enumerate(steps, start=1):
        step_obj = db.Step(recipe=recipe, description=step, order_number=i)
        db.session.add(step_obj)

    db.session.commit()

    return 'Recipe inserted successfully'