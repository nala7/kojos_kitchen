from status import Status
from utils import generate_time, is_closed


t = 0
t0 = generate_time(t)
t_a = t0
ss = Status()

while not (ss.n == 0 and is_closed(t_a)):
    if t_a == min(t_a, ss.s1.time, ss.s2.time):
        t = t_a
        t_t = generate_time(t)
        t_a = t + t_t
        if not is_closed(t_a):
            client = ss.client_arrives(t_a)
            if ss.n == 0 or not ss.client_s1:
                ss.add_client_s1(client)
            elif not ss.client_s2:
                ss.add_client_s2(client)
            else:
                ss.add_client_to_queque(client)

    elif ss.s1.time < t_a and ss.s1.time <= ss.s2.time:
        t = ss.s1.time
        ss.finish_with_client_s1()

    elif ss.s2.time < t_a and ss.s2.time <= ss.s1.time:
        t = ss.s2.time
        ss.finish_with_client_s2()
