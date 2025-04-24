import random
from operator import index

sample_titles = [
    "Creamy Tomato Pasta", "Grilled Chicken Salad", "Spicy Stir Fry Noodles",
    "Avocado Toast Deluxe", "Chickpea Curry", "Beef Tacos"
]

sample_ingredients = [
    ["pasta", "tomato", "cream", "basil"],
    ["chicken", "lettuce", "cucumber", "olive oil"],
    ["noodles", "carrot", "pepper", "soy sauce"],
    ["bread", "avocado", "egg", "chili flakes"],
    ["chickpeas", "onion", "garlic", "coconut milk"],
    ["beef", "tortilla", "cheddar", "lettuce"]
]

sample_instructions = [
    "Boil pasta. Cook sauce. Mix and garnish with basil.",
    "Grill chicken. Mix veggies. Toss with dressing.",
    "Stir-fry veggies and noodles in sauce. Serve hot.",
    "Toast bread. Mash avocado. Top with egg & seasoning.",
    "Simmer chickpeas with spices and coconut milk.",
    "Cook beef. Fill tortillas. Add toppings and enjoy."
]

sample_images = [
    "https://placehold.co/600x400?text=Tomato+Pasta",
    "https://placehold.co/600x400?text=Chicken+Salad",
    "https://placehold.co/600x400?text=Noodles",
    "https://placehold.co/600x400?text=Avocado+Toast",
    "https://placehold.co/600x400?text=Chickpea+Curry",
    "https://placehold.co/600x400?text=Beef+Tacos"
]

def generate_mock_recipe(user_ingredients: list[str]) -> dict:
    user_ingredients_set = set(ingredient.lower() for ingredient in user_ingredients)
    #Score each sample recipe by how many ingredients match
    scored = []
    for i, recipe_ingredients in enumerate(sample_ingredients):
        recipe_set = set(recipe_ingredients)
        match_score = len(user_ingredients_set & recipe_set)
        scored.append((match_score, i))

    # Sort by best match
    scored.sort(reverse=True)
    top_score, top_index = scored[0]
    return {
        "title": sample_titles[top_index],
        "ingredients": sample_ingredients[top_index],
        "instructions": sample_instructions[top_index],
        "image_url": sample_images[top_index]
    }

def generate_mock_response(user_ingredients: list[str], count: int = 3) -> list[dict]:
    # Return top 3 matching recipes instead of random
    user_ingredients_set = set(i.lower() for i in user_ingredients)
    scored = []

    for i, recipe_ingredients in enumerate(sample_ingredients):
        match_score = len(user_ingredients_set & set(user_ingredients))

    # Sort by best match and get the top `count` recipes
    scored.sort(reverse=True)
    selected_indexes = [index for _, index in scored[:count]]

    return [
        {
            "title": sample_titles[i],
            "ingredients": sample_ingredients[i],
            "instructions": sample_instructions[i],
            "image_url": sample_images[i]
        }
        for i in selected_indexes
    ]


