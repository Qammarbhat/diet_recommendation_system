from pydantic import BaseModel
from typing import List, Optional


class Params(BaseModel):
    n_neighbors: int = 5
    return_distance: bool = False


class NutritionInput(BaseModel):
    calories: float  # kcal
    fat_content: float  # g
    saturated_fat_content: float  # g
    cholesterol_content: float  # mg
    sodium_content: float  # mg
    carbohydrate_content: float  # g
    fiber_content: float  # g
    sugar_content: float  # g
    protein_content: float  # g


class PredictionInput(BaseModel):
    nutrition_input: NutritionInput
    ingredients: List[str]
    params: Params  # Changed to use the Params model


class Recipe(BaseModel):
    Name: str
    CookTime: str
    PrepTime: str
    TotalTime: str
    RecipeIngredientParts: List[str]
    Calories: float
    FatContent: float
    SaturatedFatContent: float
    CholesterolContent: float
    SodiumContent: float
    CarbohydrateContent: float
    FiberContent: float
    SugarContent: float
    ProteinContent: float
    RecipeInstructions: List[str]


class PredictionOut(BaseModel):
    output: Optional[List[Recipe]] = None
