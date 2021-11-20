from client import Client
from server import Server
from utils import create_order


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
        order = create_order()
        client = Client(order, t_a)
        self.waiting_clients.append(client)
        self.clients.append(client)
        return client

    def add_client_s1(self, client: Client):
        self.s1.take_order(client)
        self.client_s1 = client

    def finish_with_client_s1(self):
        self.client_s1 = None
        self.s1.time = 1
        self.update_count()

    def add_client_s2(self, client: Client):
        self.s2.take_order(client)
        self.client_s2 = client

    def finish_with_client_s2(self):
        self.client_s2 = None
        self.s2.time = 1
        self.update_count()

    def add_client_to_queque(self, client):
        self.waiting_clients.append(client)
