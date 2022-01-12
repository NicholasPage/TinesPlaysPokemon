#!flask/bin/python
"""Now let's build a JSON from s3. Did someone say stateful?"""
import random
import json
import subprocess

from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

allowed_keys = [A,B,Space,Up,Down,Left,Right]
	
@app.route('/TPP/api/v1.0/command', methods=['POST'])
def Input_Command():
    """Adds a recipe to the list"""
	#Example
	#curl -H "Content-Type: application/json" -X POST -d '{"name":"recipename","ingredients":"ingredient1, ingredient2, ingredient3","difficulty":"difficultylevel"}' http://localhost:5000/recipe/api/v1.0/newrecipe
  # if not request.json or not 'text' in request.json:
  #     abort(400)
  # recipe = {
  #     'id': len(recipes) + 1,
  #     'text': request.json.get('text', ""),
  #     'def': request.json.get('def', "")
  # }
  # recipes.append(recipe)
  # return jsonify({'recipe': recipe}), 201
  subprocess.call({"xdotool", "key", "request.json"})
  return jsonify("request.json"), 201
	
  
  

@app.route('/TPP/api/v1.0/DeleteRecipeById/<int:id>', methods=['DELETE'])
def Delete_RecipeById(id):
    """Delete a recipe with the provided recipeID"""
    if id not in range(1,len(recipes)):
        abort(404)
    recipe = recipes[id-1]
    recipes.remove(recipe)
    return jsonify({'Successfully removed the recipe': recipe['name']})


if __name__ == '__main__':
    app.run(debug=True)
