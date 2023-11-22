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


# function addStep() {
#     // Get user input
#     var number = document.getElementById("number").value;
#     var step = document.getElementById("step").value;
#
#     // Create a new list item
#     var listItem = document.createElement("li");
#     listItem.textContent = number + ". " + step;
#     listItem.classList.add("content"); // Add the "content" class to the list item
#
#     // Create a delete button
#     var deleteButton = document.createElement("button");
#     deleteButton.textContent = "Delete";
#     deleteButton.classList.add("button"); // Add the "button" class to the delete button
#     deleteButton.onclick = function() {
#         listItem.remove();
#     };
#
#     // Append the delete button to the list item
#     listItem.appendChild(deleteButton);
#
#     // Append the list item to the ingredient list
#     document.getElementById("ingredientStep").appendChild(listItem);
#
#     // Clear input fields
#     document.getElementById("methodForm").reset();
# }