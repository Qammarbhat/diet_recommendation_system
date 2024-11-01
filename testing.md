# Example 1: Balanced Nutrition Profile with Common Ingredients
{
  "nutrition_input": {
    "calories": 200,
    "fat_content": 8,
    "saturated_fat_content": 2,
    "cholesterol_content": 30,
    "sodium_content": 300,
    "carbohydrate_content": 30,
    "fiber_content": 4,
    "sugar_content": 5,
    "protein_content": 15
  },
  "ingredients": ["chicken", "broccoli"],
  "params": {
    "n_neighbors": 5,
    "return_distance": false
  }
}

# Example 2: Low-Calorie, High-Protein Option with Plant-Based Ingredients
{
  "nutrition_input": {
    "calories": 120,
    "fat_content": 3,
    "saturated_fat_content": 1,
    "cholesterol_content": 0,
    "sodium_content": 100,
    "carbohydrate_content": 10,
    "fiber_content": 5,
    "sugar_content": 2,
    "protein_content": 20
  },
  "ingredients": ["tofu", "spinach"],
  "params": {
    "n_neighbors": 3,
    "return_distance": true
  }
}

# Example 3: High-Calorie, High-Carb with Sweet Ingredients
{
  "nutrition_input": {
    "calories": 500,
    "fat_content": 20,
    "saturated_fat_content": 10,
    "cholesterol_content": 80,
    "sodium_content": 150,
    "carbohydrate_content": 60,
    "fiber_content": 3,
    "sugar_content": 40,
    "protein_content": 8
  },
  "ingredients": ["banana", "oats"],
  "params": {
    "n_neighbors": 5,
    "return_distance": false
  }
}

# Example 4: Low-Fat, High-Fiber Option with Low Sodium
{
  "nutrition_input": {
    "calories": 180,
    "fat_content": 2,
    "saturated_fat_content": 0.5,
    "cholesterol_content": 5,
    "sodium_content": 50,
    "carbohydrate_content": 25,
    "fiber_content": 10,
    "sugar_content": 3,
    "protein_content": 8
  },
  "ingredients": ["quinoa", "tomato"],
  "params": {
    "n_neighbors": 5,
    "return_distance": false
  }
}

# Example 5: Keto-Friendly with High Fat and Protein
{
  "nutrition_input": {
    "calories": 300,
    "fat_content": 25,
    "saturated_fat_content": 10,
    "cholesterol_content": 100,
    "sodium_content": 200,
    "carbohydrate_content": 5,
    "fiber_content": 2,
    "sugar_content": 1,
    "protein_content": 20
  },
  "ingredients": ["avocado", "eggs"],
  "params": {
    "n_neighbors": 3,
    "return_distance": true
  }
}
