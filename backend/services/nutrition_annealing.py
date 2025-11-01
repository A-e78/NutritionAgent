import math
from .data_filter import get_all_foods

class SimpleRandom:
    def __init__(self, seed=1):
        self.state = seed  

    def random(self):
        self.state = (self.state * 1103515245 + 12345) & 0x7fffffff
        return self.state / 0x7fffffff

    def randint(self, a, b):
        return a + int(self.random() * (b - a + 1))

    def choice(self, lista):
        if not lista:
            return None
        index = self.randint(0, len(lista) - 1)
        return lista[index]

def calcular_aptitud_nutricional(combinacion, objetivos_usuario):
    """
    Calcula qué tan buena es una combinación de alimentos
    Objetivos: {calorias: 2000, proteinas: 50, carbohidratos: 300, ...}
    """
    if not combinacion:
        return float('inf')

    # Calcular totales nutricionales de la combinación
    totales = {
        'calorias': 0,
        'proteinas': 0,
        'carbohidratos': 0,
        'grasas': 0
    }

    for alimento in combinacion:
        for nutriente in totales:
            if nutriente in alimento:
                totales[nutriente] += alimento[nutriente]

    # Calcular desviación de los objetivos
    desviacion_total = 0
    for nutriente, objetivo in objetivos_usuario.items():
        if nutriente in totales:
            diferencia = abs(totales[nutriente] - objetivo)
            # Normalizar por el objetivo para que todos los nutrientes pesen similar
            if objetivo > 0:
                desviacion_relativa = diferencia / objetivo
                desviacion_total += desviacion_relativa

    return desviacion_total

def generar_vecino_nutricional(combinacion_actual, todos_alimentos, rand, max_cambios=2):
    """
    Genera una combinación vecina modificando algunos alimentos
    """
    if not combinacion_actual:
        # Si no hay combinación actual, crear una nueva con 3-5 alimentos
        num_alimentos = rand.randint(3, 5)
        return [rand.choice(todos_alimentos) for _ in range(num_alimentos)]

    nueva_combinacion = combinacion_actual.copy()
    num_cambios = rand.randint(1, max_cambios)

    for _ in range(num_cambios):
        operacion = rand.randint(0, 2)  # 0: agregar, 1: quitar, 2: reemplazar

        if operacion == 0 and len(nueva_combinacion) < 8:  # Agregar alimento
            nuevo_alimento = rand.choice(todos_alimentos)
            if nuevo_alimento not in nueva_combinacion:
                nueva_combinacion.append(nuevo_alimento)

        elif operacion == 1 and len(nueva_combinacion) > 2:  # Quitar alimento
            idx = rand.randint(0, len(nueva_combinacion) - 1)
            nueva_combinacion.pop(idx)

        else:  # Reemplazar alimento
            if nueva_combinacion:
                idx = rand.randint(0, len(nueva_combinacion) - 1)
                nuevo_alimento = rand.choice(todos_alimentos)
                if nuevo_alimento not in nueva_combinacion:
                    nueva_combinacion[idx] = nuevo_alimento

    return nueva_combinacion

def exp_aproximada(x):
    """Aproximación de la exponencial para probabilidades"""
    if x > 10:
        return 0
    if x < -10:
        return 1
    return 1 + x + x*x/2 + x*x*x/6

def recocido_simulado_nutricion(objetivos_usuario, temp_inicial=1000, factor_enfriamiento=0.95, 
                               iteraciones_por_temp=100, semilla=42):
    """
    Algoritmo de recocido simulado para recomendación nutricional

    objetivos_usuario: dict con {calorias: X, proteinas: Y, carbohidratos: Z, ...}
    """
    # Cargar todos los alimentos disponibles
    todos_alimentos = get_all_foods()
    if not todos_alimentos:
        print("Error: No se pudieron cargar los alimentos")
        return [], float('inf')

    rand = SimpleRandom(semilla)

    # Estado inicial aleatorio (3-5 alimentos)
    num_inicial = rand.randint(3, 5)
    estado_actual = [rand.choice(todos_alimentos) for _ in range(num_inicial)]
    aptitud_actual = calcular_aptitud_nutricional(estado_actual, objetivos_usuario)

    mejor_estado = estado_actual.copy()
    mejor_aptitud = aptitud_actual

    print(f"Estado inicial: {len(estado_actual)} alimentos, aptitud: {aptitud_actual:.3f}")

    temperatura = temp_inicial
    iteracion = 0

    while temperatura > 0.1 and iteracion < 1000:
        for _ in range(iteraciones_por_temp):
            # Generar vecino
            vecino = generar_vecino_nutricional(estado_actual, todos_alimentos, rand)
            aptitud_vecino = calcular_aptitud_nutricional(vecino, objetivos_usuario)

            # Calcular diferencia
            delta = aptitud_vecino - aptitud_actual

            # Decidir si aceptar el nuevo estado
            if delta < 0:
                # Mejor solución, aceptar siempre
                estado_actual = vecino
                aptitud_actual = aptitud_vecino

                if aptitud_actual < mejor_aptitud:
                    mejor_estado = estado_actual.copy()
                    mejor_aptitud = aptitud_actual
                    print(f"Mejor solución encontrada: aptitud {mejor_aptitud:.3f}")

            else:
                # Solución peor, aceptar con probabilidad
                probabilidad = exp_aproximada(-delta / temperatura)
                if rand.random() < probabilidad:
                    estado_actual = vecino
                    aptitud_actual = aptitud_vecino

            iteracion += 1

        # Enfriar
        temperatura *= factor_enfriamiento

        if iteracion % 100 == 0:
            print(f"Iteración {iteracion}, temperatura: {temperatura:.2f}, aptitud: {aptitud_actual:.3f}")

    print(f"Mejor solución final: {len(mejor_estado)} alimentos, aptitud: {mejor_aptitud:.3f}")
    return mejor_estado, mejor_aptitud