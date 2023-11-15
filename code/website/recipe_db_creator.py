import sqlite3

# Create a connection object to the database file
conn = sqlite3.connect('cookbook.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create a table called Recipes with the specified columns
cur.execute('''CREATE TABLE IF NOT EXISTS Recipes (
    recipe_id INTEGER NOT NULL UNIQUE PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    cuisine_id TEXT,
    serves TEXT,
    image BLOB,
    cooking_time INTEGER,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors (author_id),
    FOREIGN KEY (cuisine_id) REFERENCES Cuisines (cuisine_id)
);
''')

cur.execute('''CREATE TABLE IF NOT EXISTS  Ingredients (
    ingredient_id INTEGER UNIQUE NOT NULL PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    quantity TEXT,
    FOREIGN KEY (recipe_id) REFERENCES Recipes (recipe_id),
);
''')

cur.execute('''CREATE TABLE IF NOT EXISTS Steps (
    step_id INTEGER PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    order INTEGER NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes (recipe_id),
);''')


cur.execute('''CREATE TABLE IF NOT EXISTS Authors (
    author_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    bio TEXT
);
'''),

cur.execute('''CREATE TABLE IF NOT EXISTS Cuisines (
    cuisine_id INTEGER NOT NULL UNIQUE PRIMARY KEY,
    cuisine_name TEXT,
);
''')

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
