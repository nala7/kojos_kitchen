import random
import numpy as np


def uniform_distribution(a: int, b: int) -> float:
    u = random.random()
    return a + (b - a) * u


def exponential_distribution(lamb, a, b) -> float:
    # intervalo de minutos entre los arribos de los clientes
    u = uniform_distribution(a, b)
    x = - (1 / lamb) * np.log(u)
    if x < 0:
        x = x * (-1)

    return x