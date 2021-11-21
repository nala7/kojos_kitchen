from status import Status
from server import Server
from utils import generate_time, is_closed, StoreScheduele


def print_waiting_list_0(clients):
    try:
        print('waiting client:', clients[0])
    except IndexError:
        print('empty list')


def run():
    t = 0
    t0 = generate_time(t)
    t_a = t0
    s1 = Server()
    s2 = Server()
    ss = Status(s1, s2)

    i = 0
    # while not (ss.n == 0 and is_closed(t_a)):
    while i < 10:
        i = i + 1
        print(t_a, s1.time, s2.time)
        if t_a == min(t_a, s1.time, s2.time):
            print("case 1")

            t = t_a
            t_t = generate_time(t)
            if not is_closed(t_a):
                client = ss.client_arrives(t_a)
                print(f"client arrives at {t_a}")
                if ss.n() == 0 and not s1.current_client:
                    s1.take_order(t, client)
                elif ss.n() == 0 and not s2.current_client:
                    s2.take_order(t, client)
                else:
                    ss.add_client_to_queque(client)
            t_a = t + t_t

            #####
            print_waiting_list_0(ss.waiting_clients)

        elif s1.time < t_a and s1.time <= s2.time:
            print('case 2')
            t = s1.time
            if ss.n() == 0:
                client = ss.client_arrives()
            ss.add_client_from_queque(t, s1)
            #####
            print_waiting_list_0(ss.waiting_clients)
        elif s2.time < t_a and s2.time <= s1.time:
            print("case 3")
            t = s2.time
            ss.add_client_from_queque(t, s2)
            #####
            print_waiting_list_0(ss.waiting_clients)
    return ss


status = run()
for customer in status.clients:
    print(customer)
print(len(status.clients))



