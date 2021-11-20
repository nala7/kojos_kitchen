import enum

class Client:
    def __init__(self, order_type : enum, t_a : int) -> None:
        self.order_type = order_type
        self.t_a = t_a
        self.t_d : int