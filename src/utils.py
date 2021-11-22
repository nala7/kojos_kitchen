from client import Client
from server import Server

from enum import Enum
from typing import List
from sys import maxsize

from distributions import exponential_distribution


class StoreSchedule(Enum):
    closing_time = 660


def generate_time(t) -> int:
    lamb = 0.5 if is_peak_time(t) else 0.2
    x = exponential_distribution(lamb, 0, 10)
    return int(x)


def generate_clientes() -> List[Client]:
    t_a = generate_time(0)
    client_list = []
    while t_a < StoreSchedule.closing_time.value:
        t_a = t_a + generate_time(t_a)
        client = Client(t_a)
        client_list.append(client)
    return client_list


def min_server_time(server_list):
    min_time = maxsize
    for server in server_list:
        min_time = min(min_time, server.time)
    return min_time


def free_server(current_time, server_list: List[Server]):
    for server in server_list:
        if not server.working or current_time > server.time:
            return server
    return None


def time_to_minutes(t: int) -> int:
    passed_hours = int(t / 100) - 10
    passed_minutes = t % 100
    return passed_hours * 60 + passed_minutes


def is_peak_time(t: int) -> bool:
    return (90 <= t <= 210) or (300 <= t <= 540)


def is_closed(t):
    return t >= StoreSchedule.closing_time.value
