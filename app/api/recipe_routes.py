from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import User, Recipe, Ingredient, Instruction

recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.get('/')
def get_all_recipes():
    all_recipes = Recipe.query.all()
    response = {'all_recipes': [recipe.post_to_dict() for recipe in all_recipes]}
    return response