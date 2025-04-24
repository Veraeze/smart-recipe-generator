import {useState} from 'react'

function RecipeForm() {
    const [ingredients, setIngredients] = useState("");
    const [useMock, setUseMock] = useState(true);
    const [loading, setLoading] = useState(false);
    const [recipes, setRecipes] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setRecipes([]);

        try {
            const res = await fetch(`http://localhost:8000/generate-recipes?use_mock=${useMock}`,{
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({ingredients: ingredients.split(",").map(i => i.trim())}),
            });

            const data = await res.json();
            setRecipes(data.recipes);
        } catch (error) {
            console.error("Error fetching recipes:", error);
        }
        setLoading(false);
    };
  return (
    <div className='space-y-6'>
      <form onSubmit={handleSubmit} className='space-y-4'>
        <textarea
        value={ingredients} onChange={(e) => setIngredients(e.target.value)}
        placeholder="e.g rice, chicken, tomato"
        className='w-full border border-primary rounded-lg p-3 bg-white text-text focus:outline-none focus:ring-2 focus:ring-primary'
        rows={4}
        />
        <label className='flex items-center gap-2 text-sm text-text'>
            <input
            type='checkbox' checked={useMock}
            onChange={() => setUseMock(!useMock)} className='accent-primary'
            />
            Use Mock AI
        </label>
        <button
        type='submit' disabled={loading}
        className='bg-primary text-white px-4 py-2 rounded hover:bg-opacity-90'>
            {loading ? "Generating..." : "Generate Recipe"}
        </button>
      </form>

      {recipes.length > 0 && (
        <div className='space-y-4'>
            {recipes.map((recipe, i) => (
                <div key={i} className='p-4 border border-primary bg-accent rounded-lg shadow'>
                    <h2 className='text-lg font-bold text-primary mb-2'>{recipe.title}</h2>
                    <p className='text-sm text-text mb-1'>
                        <strong>Ingredients:</strong> {recipe.ingredients?.join(", ") || "N/A"}
                    </p>
                    <p className='text-sm text-text mb-2'>
                        <strong>Instructions:</strong> {recipe.instructions || recipe.raw_recipe}
                    </p>
                    {recipe.image_url && (
                        <img src={recipe.image_url} alt={recipe.title}
                        className='mt-2 w-full max-h-64 object-cover rounded'
                        />
                    )}
                </div>
            ))}
        </div>
      )}
    </div>
  )
}

export default RecipeForm
