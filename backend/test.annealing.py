from services.nutrition_annealing import recocido_simulado_nutricion

def test_algoritmo():
    """Test básico del algoritmo de recocido simulado"""

    # Objetivos de ejemplo para un usuario
    objetivos_ejemplo = {
        'calorias': 2000,
        'proteinas': 50,
        'carbohidratos': 300,
        'grasas': 70
    }

    print(" Probando algoritmo de recocido simulado...")
    print(f"Objetivos: {objetivos_ejemplo}")
    print("=" * 50)

    combinacion, aptitud = recocido_simulado_nutricion(
        objetivos_ejemplo, 
        temp_inicial=1000,
        iteraciones_por_temp=50,
        semilla=42
    )

    print("\n" + "=" * 50)
    print(" RESULTADOS FINALES:")
    print(f"Aptitud de la solución: {aptitud:.3f}")
    print(f"Número de alimentos recomendados: {len(combinacion)}")

    # Mostrar la combinación recomendada
    print("\n ALIMENTOS RECOMENDADOS:")
    for i, alimento in enumerate(combinacion, 1):
        print(f"{i}. {alimento.get('nombre', 'Sin nombre')}")
        print(f"   Calorías: {alimento.get('calorias', 'N/A')}")
        print(f"   Proteínas: {alimento.get('proteinas', 'N/A')}g")
        print(f"   Carbohidratos: {alimento.get('carbohidratos', 'N/A')}g")
        print(f"   Grasas: {alimento.get('grasas', 'N/A')}g")
        print()

if __name__ == "__main__":
    test_algoritmo()