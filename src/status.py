from client import Client
from server import Server
from utils import CreateOrder


class Status:
    def __init__(self) -> None:
        self.n = 0
        self.client_s1 = None
        self.s1 = Server()
        self.client_s2 = None
        self.s2 = Server()
        self.waiting_clients = []
        self.clients = []

    def update_count(self):
        n = 0
        if self.client_s1:
            n = n + 1
        if self.client_s2:
            n = n + 1
        self.n = n + len(self.waiting_clients)

    def client_arrives(self, t_a) -> Client:
        order = CreateOrder()
        client = Client(order, t_a)
        self.waiting_clients.append(client)
        self.clients.append(client)
        return client
