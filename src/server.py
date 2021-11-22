from sys import maxsize

from client import Client, OrderType
from status import Status
from distributions import uniform_distribution


def sushi_order_time():
    x = uniform_distribution(5, 8)
    return int(x)


def sandwich_order_time():
    x = uniform_distribution(3, 5)
    return int(x)


class Server:
    def __init__(self, number) -> None:
        self.clients_served = 0
        self.working = False
        self.time = maxsize
        self.number = number

    def take_order(self, current_time: int, client: Client, ss: Status):
        self.working = True

        if client.order_type == OrderType.sushi:
            y = sushi_order_time()
        else:
            y = sandwich_order_time()

        client.t_d = client.t_a + y
        self.time = client.t_d
        client.time_waited = current_time - client.t_a
        client.server = self.number
        ss.clients_departures.append(client)

    def free_server(self):
        self.working = False
        self.time = 1


