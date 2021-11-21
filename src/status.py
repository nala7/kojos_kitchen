from client import Client
from server import Server
from utils import create_order, StoreScheduele


class Status:
    def __init__(self, server1, server2, server3 = None) -> None:
        self.waiting_clients = []
        self.clients = []

    def n(self):
        return len(self.waiting_clients)

    def client_arrives(self, t_a) -> Client:
        order = create_order()
        client = Client(order, t_a)
        self.clients.append(client)
        return client

    def add_client_from_queque(self, current_time, server):
        if self.waiting_clients:
            client = self.waiting_clients.pop()
            server.take_order(current_time, client)
        else:
            server.time = 1
            server.current_client = None

    def add_client_to_queque(self, client):
        self.waiting_clients.append(client)
