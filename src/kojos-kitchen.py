from typing import List
from client import Client
from server import Server
from utils import GenerateTime, OrderType


class KojosKitchen():
    def __init__(self) -> None:
        self.n_a = self.t = 0
        self.s1 = Server()
        self.s2 = Server()
        self.s3 = Server()
        self.ss : List(Client) = []
        self.t0 = GenerateTime()
        self.t_a = self.t0

    def Run(self):
        if self.t_a == min(self.t_a, self.s1.time, self.s2.time):
            pass

        if self.s1 < self.t_a