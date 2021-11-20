import random
import numpy as np
import math

from enum import Enum



class OrderType(Enum):
    sandwitch = 1
    sushi = 2


def uniform_distibution(a : int, b : int) -> int: 
    U = random.random()
    return a + (b - a) * U


def exponential_distribution(lamb) -> int:
    # intervalo de minutos entre los arribos de los clientes
    u = uniform_distibution(0, 15)
    x = - (1 / lamb) * np.log(u)
    if x < 0:
        x = x * (-1)

    return x


def CreateOrder():
    U = random.random()
    if U > 0.5:
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


def TimeToMinutes(t : int) -> int:
    # start_hour = 1000
    passed_hours = int(t/100) - 10
    # print(passed_hours)
    passed_minutes = t%100
    # print(passed_minutes)
    return passed_hours * 60 + passed_minutes



def GenerateTime(is_peak_time : bool) -> int:
    lamb = 0.5 if is_peak_time else 0.25
    x = exponential_distribution(lamb)

    return x, IsPeakTime(), IsClosed()


def IsPeakTime(t : int) -> bool:
    return (t >= 90 and t <= 210) or (t >= 300 and t<= 540)


def IsClosed(t):
    return t >= 660


def SushiOrderTime():
    x = uniform_distibution(5, 8)
    return x


def SandwichOrderTime():
    x = uniform_distibution(3, 5)
    return x    

print(1130, TimeToMinutes(1130))
print(1330, TimeToMinutes(1330))
print(1700, TimeToMinutes(1500))
print(1900, TimeToMinutes(1900))
print(2100, TimeToMinutes(2100))
