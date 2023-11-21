from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')


app.config['DATABASE'] = 'cookbook.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cookbook.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/recipe/<recipe_name>')
def serveRecipe(recipe_id):
    
    # Query the database to get the recipe details
    recipe = db.Recipe.query.filter_by(recipe_id=recipe_id).first()

    recipe_name = recipe.name

    # Get related data (e.g., ingredients and steps)
    ingredients = recipe.ingredients
    steps = recipe.steps
    author_name = recipe.author.name
    email = recipe.author.email
    serves = recipe.serves
    image = recipe.image  # Assuming image is stored as binary data
    time = recipe.cooking_time
    cuisine_name = recipe.cuisine.cuisine_name

    return render_template("build_recipe.html", 
                           author_name=author_name,
                           email=email,
                           recipe_name=recipe_name,
                           recipe_desc=recipe.description,
                           serves=serves,
                           image=image,
                           time=time,
                           ingredients=ingredients,
                           steps=steps,
                           cuisine_name=cuisine_name)


@app.route('/search')
def search():
    query = request.args.get('query')

    # Perform a search in the database based on the query
    results = perform_search(query)

    return render_template('search_results.html', query=query, results=results)

def perform_search(query):
    # Example: Search for recipes or cuisines containing the query in name or description


    cuisine_results = db.Cuisine.query.filter(db.Cuisine.cuisine_name.ilike(f"%{query}%")).all()

    recipe_results = db.Recipe.query.filter(
        (db.Recipe.name.ilike(f"%{query}%")) | (db.Recipe.description.ilike(f"%{query}%"))
    ).all()

    return {'recipes': recipe_results, 'cuisines': cuisine_results}


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