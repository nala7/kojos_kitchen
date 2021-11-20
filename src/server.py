import sys

from client import Client
from utils import OrderType, SushiOrderTime, SandwichOrderTime

class Server():
    def __init__(self) -> None:
        self.started_working = False
        self.clients_served = 0
        self.time = sys.maxint
        

    def TakeOrder(self, client : Client):
        self.started_working = True
        self.clients_served = self.clients_served + 1
        # Handle order: set client.t_d
        if client.order_type == OrderType.sushi:
            y = SushiOrderTime()
        else:
            y = SandwichOrderTime()

        self.time = self.time + y
        client.t_d = client.t_a + y

