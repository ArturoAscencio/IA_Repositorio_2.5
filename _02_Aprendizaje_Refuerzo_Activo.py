# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install gym

import gym
import numpy as np

# Crear el entorno "Taxi-v3"
env = gym.make("Taxi-v3")

# Configuración del algoritmo Q-learning
num_episodes = 1000
learning_rate = 0.1
discount_factor = 0.99
exploration_prob = 0.2

# Inicializar la tabla Q con ceros
num_states = env.observation_space.n
num_actions = env.action_space.n
Q = np.zeros((num_states, num_actions)

# Ciclo de entrenamiento
for episode in range(num_episodes):
    state = env.reset()
    done = False

    while not done:
        # Elegir una acción con epsilon-greedy
        if np.random.rand() < exploration_prob:
            action = env.action_space.sample()  # Exploración
        else:
            action = np.argmax(Q[state, : )  # Explotación

        # Realizar la acción y obtener la observación, recompensa y si el episodio termina
        next_state, reward, done, _ = env.step(action)

        # Actualizar la tabla Q
        Q[state, action] = Q[state, action] + learning_rate * (reward + discount_factor * np.max(Q[next_state, :]) - Q[state, action])

        state = next_state

# Evaluar la política óptima aprendida
state = env.reset()
done = False
total_reward = 0

while not done:
    action = np.argmax(Q[state, :])
    next_state, reward, done, _ = env.step(action)
    total_reward += reward
    state = next_state

print(f"Recompensa total con la política óptima: {total_reward}")
