from flask import Flask, render_template, request, db
import sqlite3

app = Flask(__name__, static_url_path='/static')
app.config['DATABASE'] = 'cookbook.db'

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

@app.route('/publish', methods=['POST'])
def publish():
    authorName = request.form['authorname']
    email = request.form['email']
    recipeName = request.form['recipename']
    recipeDesc = request.form['rescipedesc']
    serves = request.form['serves']
    image = request.form['image']
    time = request.form['time']
    ingredients = request.form['ingredients'] #list of pairs(ingredient, quantity)
    steps = request.form['steps'] # list of steps in order
    cuisine = request.form['cuisine']

    #Populate Cuisines Table
    cuisineList = ('''SELECT name FROM Cuisines;''').fetchall() #Creates a list of all cuisines already in the database
    if cuisine not in cuisineList:
        db.execute('''INSERT INTO Cuisines (cuisine_id, cuisine_name) VALUES (1, ?);''', (cuisine))

    cuisineID = db.execute('''SELECT cuisine_id FROM Cuisines WHERE cuisine_name = ?;''', (cuisine)).fetchone()[0]

    #Populate Authors Table
    db.execute('''INSERT INTO Authors (author_id, name, email, bio) 
                VALUES (1, ?, ?, '');''', (authorName, email))

    authorID = db.execute('''SELECT author_id FROM Authors WHERE name=?;''', (authorName)).fetchone()[0]

    #Populate Recipes Table
    db.execute('''INSERT INTO Recipes (recipe_id, name, description, cuisine_id, serves, image, cooking_time, author_id) 
                VALUES (1, ?, ?, ?, ?, ?, ?, ?);''', (recipeName, recipeDesc,cuisineID, serves, image, time, authorID))

    recipeID = db.execute('''SELECT recipe_id FROM Recipes WHERE name=?;''', (recipeName)).fetchone()[0]

    #Populate Ingredients Table
    for ingredient in ingredients:
        db.execute('''INSERT INTO Ingredients (ingredient_id, recipe_id, name, quantity) 
                    VALUES (1, ?, ?, ?);''', (recipeID, ingredient[0], ingredient[1]))

    #Populate Steps Table
    i=1
    for step in steps:
        db.execute('''INSERT INTO Steps (step_id, recipe_id, description, order_number) 
                    VALUES (1, ?, ?, ?);''', (recipeID,step, i))
        i+=1

    return 'Recipe inserted successfully'
