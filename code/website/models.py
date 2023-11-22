from flask import Flask
from app import app, db

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))

class Cuisine(db.Model):
    cuisine_id = db.Column(db.Integer, primary_key=True)
    cuisine_name = db.Column(db.String(255))

class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisine.cuisine_id'))
    serves = db.Column(db.String(255), nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'))
    cuisine = db.relationship('Cuisine', backref='recipes')
    author = db.relationship('Author', backref='recipes')

class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True, unique=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.String(255), nullable=False)
    recipe = db.relationship('Recipe', backref='ingredients')

class Step(db.Model):
    step_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    order_number = db.Column(db.Integer, nullable=False)
    recipe = db.relationship('Recipe', backref='steps')

# Create the tables (run this once to create the tables)
with app.app_context():
    db.create_all()