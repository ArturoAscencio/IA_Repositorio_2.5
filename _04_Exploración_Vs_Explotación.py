# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import random

# Definir el n�mero total de acciones posibles
num_actions = 5

# Configurar el factor de exploraci�n (epsilon)
epsilon = 0.2  # Probabilidad de exploraci�n

# Funci�n para tomar una decisi�n basada en exploraci�n o explotaci�n
def tomar_decision():
    if random.random() < epsilon:
        # Exploraci�n: elige una acci�n aleatoria
        return random.randint(0, num_actions - 1)
    else:
        # Explotaci�n: elige la mejor acci�n conocida
        return obtener_mejor_accion()

# Simular un agente que toma decisiones en un entorno
for _ in range(10):
    accion_elegida = tomar_decision()
    print(f"El agente elige la acci�n {accion_elegida}")
