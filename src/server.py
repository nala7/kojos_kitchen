import sys
from client import Client
from utils import OrderType, sushi_order_time, sandwich_order_time,StoreScheduele


class Server:
    def __init__(self) -> None:
        self.clients_served = 0
        self.current_client = None
        self.time = sys.maxsize

    def take_order(self, current_time: int, client: Client):
        self.current_client = client
        self.clients_served = self.clients_served + 1
        # Handle order: set client.t_d
        if client.order_type == OrderType.sushi:
            y = sushi_order_time()
        else:
            y = sandwich_order_time()

        if self.time > StoreScheduele.closing_time.value:
            self.time = current_time
        self.time = self.time + y
        client.t_d = client.t_a + y
        client.time_waited = current_time - client.t_a

