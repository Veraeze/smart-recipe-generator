from fastapi import APIRouter
from app.models.ingredient_input import IngredientInput

router = APIRouter()

@router.post("/generate-recipes")
def generate_recipes(data: IngredientInput):
    #logic
    sample_recipe = {
        "title": "fried rice and chicken",
        "ingredients_used": data.ingredients,
        "instructions": "Cook rice, add pepper,vegetables and chicken. Simmer for 20 minutes.",
        "image_url": "https://example.com/spicy-chicken-rice.jpg"
    }

    return {"recipes": [sample_recipe]}