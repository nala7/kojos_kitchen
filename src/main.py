from status import Status
from server import Server
from client import Client
from utils import generate_clientes, is_closed, free_server, is_peak_time

from typing import List
from sys import maxsize


def receive_client(ss: Status, client_list: List[Client], server_list: List[Server]):
    client = client_list.pop(0)
    current_time = client.t_a

    server = free_server(current_time, server_list)
    if server:
        server.take_order(current_time, client, ss)
    else:
        ss.waiting_clients.append(client)
    return current_time


def serve_client(with_3_servers, current_time, ss: Status, server_list: List[Server]):
    if with_3_servers:
        if is_peak_time(current_time) and len(server_list) == 2:
            server_list.append(Server(3))

        if not is_peak_time(current_time) and len(server_list) == 3:
            server_list.pop(2)

    min_t_server = maxsize
    server = None
    for i in range(len(server_list)):
        if min_t_server > server_list[i].time > 1:
            min_t_server = server_list[i].time
            server = server_list[i]

    current_time = min_t_server
    if ss.waiting_clients:
        client = ss.waiting_clients.pop()
        server.take_order(current_time, client, ss)
    elif server:
        server.free_server()

    return current_time


def min_served_finished(server_list):
    min_time = maxsize
    for server in server_list:
        if min_time > server.time > 1:
            min_time = server.time
    return min_time


def clients_in_shop(server_list: List[Server], ss: Status):
    if not ss.n() == 0:
        return True
    for server in server_list:
        if server.working:
            return True
    return False


def run(with_3_servers) -> Status:
    t = 0
    server_list = [Server(1), Server(2)]
    client_list = generate_clientes()
    ss = Status(server_list)

    while not (ss.n() == 0 and is_closed(t)):
        if not client_list:
            break
        t_a = client_list[0].t_a
        if t_a <= min_served_finished(server_list) or (not clients_in_shop):
            t = receive_client(ss, client_list, server_list)
        else:
            t = serve_client(with_3_servers, t, ss, server_list)

    return ss


times_with_3_servers_was_better = 0
for i in range(100):
    status_2_servers = run(False)
    time_exceded_with_2_servers = 0
    for c in status_2_servers.clients_departures:
        if c.time_waited >= 5:
            time_exceded_with_2_servers = time_exceded_with_2_servers + 1

    status_3_servers = run(True)
    time_exceded_with_3_servers = 0
    for c in status_3_servers.clients_departures:
        if c.time_waited >= 5:
            time_exceded_with_3_servers = time_exceded_with_2_servers + 1

    print("Clients that waited more that 5 minuted to be served with 2 chefs: ", time_exceded_with_2_servers)
    print("Clients that waited more that 5 minuted to be served with 3 chefs: ", time_exceded_with_3_servers)

    if time_exceded_with_3_servers < time_exceded_with_2_servers:
        times_with_3_servers_was_better = times_with_3_servers_was_better + 1
print(f'{times_with_3_servers_was_better} times out of a 100 it was better to have 3 chefs during rush hours')
