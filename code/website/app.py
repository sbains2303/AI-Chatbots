from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__, static_url_path='/static')
app.config['DATABASE'] = 'cookbook.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipe/<recipe_name>')
def serveRecipe(recipe_name):
    
    return render_template("build_recipe.html")


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
    cur = get_db().cursor()
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
    cuisineList = cur.execute('''SELECT name FROM Cuisines;''').fetchall() #Creates a list of all cuisines already in the database
    if cuisine not in cuisineList:
        cur.execute('''INSERT INTO Cuisines (cuisine_name) VALUES (?);''', (cuisine))

    cuisineID = cur.execute('''SELECT cuisine_id FROM Cuisines WHERE cuisine_name = ?;''', (cuisine)).fetchone()[0]

    #Populate Authors Table
    cur.execute('''INSERT INTO Authors (name, email) 
                VALUES (?, ?);''', (authorName, email))

    authorID = cur.execute('''SELECT author_id FROM Authors WHERE name=?;''', (authorName)).fetchone()[0]

    #Populate Recipes Table
    cur.execute('''INSERT INTO Recipes (name, description, cuisine_id, serves, image, cooking_time, author_id) 
                VALUES (?, ?, ?, ?, ?, ?, ?);''', (recipeName, recipeDesc,cuisineID, serves, image, time, authorID))

    recipeID =  cur.execute('''SELECT recipe_id FROM Recipes WHERE name=?;''', (recipeName)).fetchone()[0]

    #Populate Ingredients Table
    for ingredient in ingredients:
        cur.execute('''INSERT INTO Ingredients (recipe_id, name, quantity) 
                    VALUES (?, ?, ?);''', (recipeID, ingredient[0], ingredient[1]))

    #Populate Steps Table
    i=1
    for step in steps:
        cur.execute('''INSERT INTO Steps (recipe_id, description, order_number) 
                    VALUES (?, ?, ?);''', (recipeID,step, i))
        i+=1

    return 'Recipe inserted successfully'

@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()