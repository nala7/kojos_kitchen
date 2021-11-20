from status import Status
from utils import GenerateTime


class KojosKitchen:
    def __init__(self) -> None:
        self.n_a = self.t = 0
        self.t0 = GenerateTime()
        self.t_a = self.t0
        self.is_peak_time, self.is_closed = False
        self.ss = Status()

    def run(self):
        if self.t_a == min(self.t_a, self.ss.s1.time, self.ss.s2.time):
            if self.ss.n == 0:
                pass

        elif self.ss.s1.time < self.t_a and self.ss.s1.time <= self.ss.s2.time:
            pass
            
        elif self.ss.s2.time < self.t_a and self.ss.s2.time <= self.ss.s1.time:
            pass
