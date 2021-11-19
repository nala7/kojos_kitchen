from typing import List
from client import Client
from server import Server
from utils import GenerateTime, IsPickTime

ss : List(Client) = []
n_a = t = 0
s1 = Server()
s2 = Server()
s3 = Server()
ss : List(Client) = []
t0 = GenerateTime()
t_a = t0

if IsPickTime():
    if t_a == min(t_a, s1.time, s2.time, s3.time):
        pass
    if s1.time < t_a and s1.time <= min(s2.time, s3.time):
        pass
    if s2.time < t_a and s2.time <= min(s1.time, s3.time):
        pass
    if s3.time < t_a and s3.time <= min(s1.time, s2.time):
        pass


else:
    if t_a == min(t_a, s1.time, s2.time):
        pass

    if s1.time < t_a and s1.time <= s2.time:
        pass

    if s2.time < t_a and s2.time <= s1.time:
        pass

