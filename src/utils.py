import random
import numpy as np

from enum import Enum


class OrderType(Enum):
    sandwich = 1
    sushi = 2


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


def create_order():
    u = random.random()
    if u > 0.5:
        return OrderType.sandwitch
    return OrderType.sushi


def test():
    # 0-5, 5-10, 10-15
    times = [0, 0, 0]
    for i in range(1000):
        x = exponential_distribution(0.5, 0, 15)
        if x < 5:
            times[0] = times[0] + 1
        elif x < 10:
            times[1] = times[1] + 1
        elif x < 15:
            times[2] = times[2] + 1
        # print(x)
    print(times)


def time_to_minutes(t: int) -> int:
    # start_hour = 1000
    passed_hours = int(t / 100) - 10
    # print(passed_hours)
    passed_minutes = t % 100
    # print(passed_minutes)
    return passed_hours * 60 + passed_minutes


def generate_time(t) -> int:
    lamb = 0.5 if is_peak_time(t) else 0.25
    # time between the arrival of two clients is set between 0 and 15 minutes
    x = exponential_distribution(lamb, 0, 15)
    return int(x)


def is_peak_time(t: int) -> bool:
    return (90 <= t <= 210) or (300 <= t <= 540)


def is_closed(t):
    return t >= 660


def sushi_order_time():
    x = uniform_distribution(5, 8)
    return x


def sandwich_order_time():
    x = uniform_distribution(3, 5)
    return x


print(1130, time_to_minutes(1130))
print(1330, time_to_minutes(1330))
print(1700, time_to_minutes(1500))
print(1900, time_to_minutes(1900))
print(2100, time_to_minutes(2100))
