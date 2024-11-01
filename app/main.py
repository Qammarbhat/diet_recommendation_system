from fastapi import FastAPI, HTTPException
import pandas as pd
from src.model import recommend, output_recommended_recipes
from app.schema import PredictionInput, Recipe  # Import the Pydantic models

# Load your dataset
dataset = pd.read_csv('dataset.csv', compression='gzip')

app = FastAPI()

@app.get("/")
def root():
    return {"Health": "Service is up and running"}

@app.post("/recommend/")
async def get_recommendations(prediction_input: PredictionInput):
    # Convert NutritionInput to a list of values
    nutrition_values = [
        prediction_input.nutrition_input.calories,
        prediction_input.nutrition_input.fat_content,
        prediction_input.nutrition_input.saturated_fat_content,
        prediction_input.nutrition_input.cholesterol_content,
        prediction_input.nutrition_input.sodium_content,
        prediction_input.nutrition_input.carbohydrate_content,
        prediction_input.nutrition_input.fiber_content,
        prediction_input.nutrition_input.sugar_content,
        prediction_input.nutrition_input.protein_content,
    ]
    
    recommendation_dataframe = recommend(
        dataset,
        nutrition_values,  # Pass the list of numerical values
        prediction_input.ingredients,
        prediction_input.params.dict()  # Ensure params is passed as a dictionary
    )
    
    if recommendation_dataframe is None:
        raise HTTPException(status_code=404, detail="No recommendations found.")
    
    # Process the output as needed
    recommendations = output_recommended_recipes(recommendation_dataframe)
    return {"recommendations": recommendations}
