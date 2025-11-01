from fastapi import FastAPI
from services.data_filter import get_all_foods, get_filtered_foods
from services.nutrition_annealing import recocido_simulado_nutricion
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class NutritionGoals(BaseModel):
    calorias: float
    proteinas: float
    carbohidratos: float
    grasas: float

@app.get("/")
def read_root():
    return {"message": "NutritionAgent API"}

@app.get("/foods")
def get_foods():
    return get_all_foods()

@app.get("/foods/filter")
def filter_foods(max_cal: int, max_carbs: int):
    return get_filtered_foods(max_cal, max_carbs)

@app.post("/recommend")
def recommend_foods(goals: NutritionGoals):
    """
    Endpoint para obtener recomendaciones usando recocido simulado
    """
    objetivos = {
        'calorias': goals.calorias,
        'proteinas': goals.proteinas,
        'carbohidratos': goals.carbohidratos,
        'grasas': goals.grasas
    }

    combinacion_recomendada, aptitud = recocido_simulado_nutricion(objetivos)

    # Calcular totales de la combinación recomendada
    totales = {'calorias': 0, 'proteinas': 0, 'carbohidratos': 0, 'grasas': 0}
    for alimento in combinacion_recomendada:
        for nutriente in totales:
            if nutriente in alimento:
                totales[nutriente] += alimento[nutriente]

    return {
        "recomendacion": combinacion_recomendada,
        "aptitud": aptitud,
        "totales": totales,
        "objetivos": objetivos,
        "num_alimentos": len(combinacion_recomendada)
    }