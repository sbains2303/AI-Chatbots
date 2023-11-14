import sqlite3

# Create a connection object to the database file
conn = sqlite3.connect('cookbook.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create a table called Recipes with the specified columns
cur.execute('''CREATE TABLE Recipes (
    recipe_id INTEGER NOT NULL UNIQUE AUTOINCREMENT PRIMARY KEY
    name TEXT NOT NULL,
    description TEXT,
    cuisine TEXT,
    serves TEXT,
    image VARBINARY (MAX);
    cooking_time INTEGER,
    author_id INTEGER,
    ADD FOREIGN KEY (author_id) REFERENCES Authors (author_id);
)''')

cur.execute('''CREATE TABLE Ingredients (
    ingredient_id INTEGER UNIQUE NOT NULL AUTOINCREMENT PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    quantity TEXT,
    FOREIGN KEY (recipe_id) REFERENCES Recipes (recipe_id)
)
''')

cur.execute('''CREATE TABLE Steps (
    step_id INTEGER PRIMARY KEY,
    recipe_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    order INTEGER NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes (recipe_id)
);''')


cur.execute('''CREATE TABLE Authors (
    author_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    bio TEXT
);
''')



# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
