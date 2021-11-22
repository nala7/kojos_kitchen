import random

from enum import Enum


class OrderType(Enum):
    sandwich = 1
    sushi = 2


def create_order():
    u = random.random()
    if u > 0.5:
        return OrderType.sandwich
    return OrderType.sushi


class Client:
    def __init__(self, t_a: int) -> None:
        self.order_type = create_order()
        self.t_a = t_a
        self.t_d: int = -1
        self.time_waited: int = -1
        self.server = -1

    def __str__(self):
        text = f'Order: {self.order_type}, AT: {self.t_a}, DT: {self.t_d}, ' \
               f'WT: {self.time_waited}, Server: {self.server}'
        return text
