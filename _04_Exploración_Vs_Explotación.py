# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import random

# Definir el número total de acciones posibles
num_actions = 5

# Configurar el factor de exploración (epsilon)
epsilon = 0.2  # Probabilidad de exploración

# Función para tomar una decisión basada en exploración o explotación
def tomar_decision():
    if random.random() < epsilon:
        # Exploración: elige una acción aleatoria
        return random.randint(0, num_actions - 1)
    else:
        # Explotación: elige la mejor acción conocida
        return obtener_mejor_accion()

# Simular un agente que toma decisiones en un entorno
for _ in range(10):
    accion_elegida = tomar_decision()
    print(f"El agente elige la acción {accion_elegida}")
