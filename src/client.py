import enum
from utils import create_order


class Client:
    def __init__(self, order_type: enum, t_a: int) -> None:
        self.order_type = order_type
        self.t_a = t_a
        self.t_d: int
        self.time_waited: int

    def __str__(self):
        text = f'Order: {self.order_type}, AT: {self.t_a}'
        return text
