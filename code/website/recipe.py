from flask import g
import sqlite3

DATABASE = "cookbook.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


class recipe():
    def __init__(self, recipe_id):
        cur = get_db().cursor()
        self.recipe_name = cur.execute("SELECT * FROM Recipes")
