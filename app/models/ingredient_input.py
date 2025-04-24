from pydantic import BaseModel
from typing import List

class IngredientInput(BaseModel):
    ingredients: List[str]