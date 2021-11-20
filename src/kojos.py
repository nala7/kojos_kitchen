from typing import List
from client import Client
from server import Server
from status import Status
from utils import GenerateTime, IsPeakTime, CreateOrder


class KojosKitchen():
    def __init__(self) -> None:
        pass


    def OpenKitchen(self):
        self.n_a = self.t = 0
        self.t0 = GenerateTime()
        self.t_a = self.t0
        self.is_peak_time, self.is_closed = False
        self.ClientArrives(self.t_a)


    def Run(self):
        # 3 servidores
        if self.is_peak_time:
            if self.t_a == min(self.t_a, self.s1.time, self.s2.time, self.s3.time):
                pass
            if self.s1.time < self.t_a and self.s1.time <= min(self.s2.time, self.s3.time):
                pass
            if self.s2.time < self.t_a and self.s2.time <= min(self.s1.time, self.s3.time):
                pass
            if self.s3.time < self.t_a and self.s3.time <= min(self.s1.time, self.s2.time):
                pass


        else:
            if self.t_a == min(self.t_a, self.s1.time, self.s2.time):
                if self.ss.n == 0:
                    pass


            elif self.s1.time < self.t_a and self.s1.time <= self.s2.time:
                pass
                
            elif self.s2.time < self.t_a and self.s2.time <= self.s1.time:
                pass


