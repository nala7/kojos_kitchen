from status import Status
from utils import generate_time


class KojosKitchen:
    def __init__(self) -> None:
        self.t = 0
        self.t0 = generate_time(self.t)
        self.t_a = self.t0
        self.is_peak_time = self.is_closed = False
        self.ss = Status()

    def run(self):
        if self.t_a == min(self.t_a, self.ss.s1.time, self.ss.s2.time):
            self.t = self.t_a
            t_t = generate_time(self.t)
            self.t_a = self.t + t_t
            client = self.ss.client_arrives(self.t_a)
            if self.ss.n == 0 or not self.ss.client_s1:
                self.ss.add_client_s1(client)
            elif not self.ss.client_s2:
                self.ss.add_client_s2(client)
            else:
                self.ss.add_client_to_queque(client)

        elif self.ss.s1.time < self.t_a and self.ss.s1.time <= self.ss.s2.time:
            self.t = self.ss.s1.time
            self.ss.finish_with_client_s1()
            
        elif self.ss.s2.time < self.t_a and self.ss.s2.time <= self.ss.s1.time:
            self.t = self.ss.s2.time
            self.ss.finish_with_client_s2()
