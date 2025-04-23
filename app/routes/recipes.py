from fastapi import Query

from fastapi import APIRouter
from app.models.ingredient_input import IngredientInput
from app.utils.ai_generator import generate_recipe
from app.utils.mock_ai import generate_mock_recipe
import asyncio

router = APIRouter()

@router.post("/generate-recipes")
async def generate_recipes(data: IngredientInput, use_mock: bool = Query(False, title="Toggle to use mock response")):
    # simulate loading time
    await asyncio.sleep(2)

    if use_mock:
        ai_response = generate_mock_recipe(data.ingredients)
    else:
        ai_response = generate_recipe(data.ingredients)

    return {"recipes": [ai_response]}