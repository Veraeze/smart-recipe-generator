import RecipeForm from "./components/RecipeForm";

function App() {

  return (
    <div className="min-h-screen bg-background text-text px-4 py-8">
      <div className="max-w-3xl mx-auto bg-white shadow-md rounded-xl p-6">
        <h1 className="text-3xl font-bold text-primary mb-4">
          Smart Recipe Generator
        </h1>
        <RecipeForm/>
      </div>
    </div>
  )
}

export default App
