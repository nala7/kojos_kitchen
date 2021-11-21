from status import Status
from utils import generate_time, is_closed


def print_waiting_list_0(clients):
    try:
        print('waiting client:', clients[0])
    except IndexError:
        print('empty list')


def run():
    t = 0
    t0 = generate_time(t)
    t_a = t0
    ss = Status()

    i = 0
    # while not (ss.n == 0 and is_closed(t_a)):
    while i < 10:
        i = i + 1
        print(t_a, ss.s1.time, ss.s2.time)
        if t_a == min(t_a, ss.s1.time, ss.s2.time):
            print("case 1")
            t = t_a
            t_t = generate_time(t)
            if not is_closed(t_a):
                client = ss.client_arrives(t_a)

                #####
                print_waiting_list_0(ss.waiting_clients)

                if ss.n == 0 or not ss.client_s1:
                    # el tiempo de espera fue 0
                    ss.add_client_s1(t_a)
                elif not ss.client_s2:
                    ss.add_client_s2(t_a)
                else:
                    ss.add_client_to_queque(client)
                t_a = t + t_t
                ss.client_arrives(t_a)

            #####
            print_waiting_list_0(ss.waiting_clients)

        elif ss.s1.time < t_a and ss.s1.time <= ss.s2.time:
            print('case 2')
            t = ss.s1.time
            ss.add_client_from_queque_s1(t)
            #####
            print_waiting_list_0(ss.waiting_clients)
        elif ss.s2.time < t_a and ss.s2.time <= ss.s1.time:
            print("case 3")
            t = ss.s2.time
            ss.add_client_from_queque_s2(t)
            #####
            print_waiting_list_0(ss.waiting_clients)
    return ss


status = run()
for customer in status.clients:
    print(customer)
print(len(status.clients))



