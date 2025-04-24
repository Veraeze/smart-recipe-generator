import random

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

def generate_mock_recipe(ingredients: list[str]) -> dict:
    idx = random.randint(0, len(sample_titles) - 1)
    return {
        "title": sample_titles[idx],
        "ingredients": sample_ingredients[idx],
        "instructions": sample_instructions[idx],
        "image_url": sample_images[idx]
    }

def generate_mock_response(user_ingredients: list[str], count: int = 3) -> list[dict]:
    return [generate_mock_recipe(user_ingredients) for _ in range(count)]

