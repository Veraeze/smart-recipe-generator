import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# client =OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recipe(ingredients: str):
    use_mock = os.getenv("USE_MOCK_AI", "False").lower() == "true"

    if use_mock:
        return f"""
        Recipe for ingredients: {', '.join(ingredients)}
        
        - Mix all ingredients in a bowl.
        - Cook on medium heat for 20 minutes.
        - Serve with a smile
        """

    #otherwise, call the real openai api
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": f"Generate a recipe using these ingredients: {', '.join(ingredients)}"
            }
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()

