class Status:
    def __init__(self, server_list) -> None:
        self.server_list = server_list
        self.waiting_clients = []
        self.clients_arrived = []
        self.clients_departures = []

    def __str__(self):
        text = f'Active servers: {len(self.server_list)}, ' \
               f'Waiting: {len(self.waiting_clients)}, Arrived: ' \
               f'{len(self.clients_arrived)}'
        return text

    def n(self):
        return len(self.waiting_clients)

    def add_client_from_queque(self, current_time, server):
        if self.waiting_clients:
            client = self.waiting_clients.pop()
            server.take_order(current_time, client)
        else:
            server.time = 1
            server.current_client = None

    def add_client_to_queque(self, client):
        self.waiting_clients.append(client)
