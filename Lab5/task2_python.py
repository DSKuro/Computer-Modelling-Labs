import math
import numpy as np

class Customer:
    def __init__(self, arrival_time, service_time):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.start_service_time = None
        self.finish_time = None

class Server:
    def __init__(self):
        self.current_customer = None
        self.finish_time = 0

    def is_available(self, current_time):
        return self.current_customer is None or current_time >= self.finish_time

    def start_service(self, customer, current_time):
        self.current_customer = customer
        self.start_service_time = current_time
        self.finish_time = current_time + customer.service_time
        customer.start_service_time = current_time

    def finish_service(self):
        finished_customer = self.current_customer
        self.current_customer = None
        return finished_customer


class QueueLimited:
    def __init__(self, max_length):
        self.customers = []
        self.max_length = max_length

    def add_customer(self, customer):
        if self.max_length is None or len(self.customers) < self.max_length:
            self.customers.append(customer)
            print(f"Клиент пришел в очередь, очередь: {len(self.customers)}")
            return True
        else:
            print("Очередь полна, клиент уходит.")
            return False

    def remove_customer(self):
        if self.customers:
            return self.customers.pop(0)
        return None


class System:
    def __init__(self, num_servers, max_queue_length, arrival_rate, service_time, ignore):
        self.servers = [Server() for _ in range(num_servers)]
        self.max_queue_length = max_queue_length
        self.queue = QueueLimited(max_queue_length)
        self.time = 0.0
        self.arrival_rate = arrival_rate
        self.service_time = service_time
        self.customers_served = 0
        self.rejected = 0
        self.queue_length = []
        self.ignore = ignore
        self.server_logs = {}
        for i in range(num_servers):
            self.server_logs[i] = 0

    def simulate(self, total_time):
        while self.time < total_time:
            self.time += np.random.poisson() if self.ignore else self.arrival_rate
            new_customer = Customer(self.time, np.random.exponential() if self.ignore else self.service_time)

            self.queue_length.append(len(self.queue.customers))
            i = 0
            for server in self.servers:
                if server.is_available(self.time):
                    print(f"Клиент обслуживается, время начала обслуживания {self.time:.2f}, на {i} канале")
                    server.start_service(new_customer, self.time)
                    self.customers_served += 1
                    self.server_logs[i] += 1
                    break
                i += 1
            else:
                if not self.queue.add_customer(new_customer):
                    self.rejected += 1

            i = 0
            for server in self.servers:
                if server.current_customer and self.time >= server.finish_time:
                    finished_customer = server.finish_service()
                    self.queue.remove_customer()
                    finished_customer.finish_time = server.finish_time
                    print(f"Клиент закончил обслуживание, время конца обслуживания {finished_customer.finish_time:.2f}, на {i} канале")
                i += 1

    def save_log(self):
        f = open("log.txt", "w+", encoding='utf-8')
        f.writelines('Количество обслуживаний по каналам:\n')
        for i in self.server_logs.keys():
            f.writelines(f'{i} канал обслужил {self.server_logs[i]} клиентов\n')
        f.writelines(f'Общая вероятность обслуживания: {self.p_served:.2f}\n')
        f.writelines(f'Общая вероятность отказа: {self.p_rejection:.2f}\n')
        f.writelines(f'Длина очереди: {self.avg_len:.2f}')
        f.close()

    def get_values(self):
        total_clients = self.customers_served + self.rejected
        if total_clients == 0:
            return 0, 0
        self.p_rejection = self.rejected / total_clients
        self.p_served = self.customers_served / total_clients
        self.avg_len = sum(self.queue_length) / len(self.queue_length)
        return self.p_rejection, self.p_served, self.avg_len

    def get_theoretical(self):
        mu = 1 / self.service_time
        len_serv = len(self.servers)
        po = self.arrival_rate / (len_serv * mu)

        if self.max_queue_length is None:
            sum_term = sum((self.arrival_rate / mu) ** k / math.factorial(k) for k in range(len_serv))
            p0 = 1 / (sum_term + ((self.arrival_rate / mu) ** len_serv) / (
                        math.factorial(len_serv) * (1 - po)))
            p_reject = 0
            lq = (p0 * (self.arrival_rate / mu) ** len_serv * po) / (
                        math.factorial(len_serv) * (1 - po) ** 2)
        else:
            sum_term = sum((self.arrival_rate / mu) ** k / math.factorial(k) for k in range(len_serv + 1))
            sum_term += sum(
                ((self.arrival_rate / mu) ** (len_serv + i)) / (
                            math.factorial(len_serv) * (len_serv ** i))
                for i in range(1, self.max_queue_length + 1))
            p0 = 1 / sum_term
            p_reject = ((self.arrival_rate / mu) ** (len_serv + self.max_queue_length)) / (
                    math.factorial(len_serv) * (len_serv ** self.max_queue_length)) * p0
            lq = sum((k - len_serv) * ((self.arrival_rate / mu) ** k) / (
                    math.factorial(len_serv) * (len_serv ** (k - len_serv))) * p0
                     for k in range(len_serv + 1, len_serv + self.max_queue_length + 1))

        return p_reject, 1 - p_reject, lq

if __name__ == "__main__":
    num_servers = 5
    max_queue_length = 3
    total_time = 3000
    arrival_time = 0.8
    service_time = 1

    system = System(num_servers, max_queue_length, arrival_time, service_time, True)
    system.simulate(total_time)

    p_reject, p_accept, avg = system.get_values()
    print(f'Вероятность отказа: {p_reject:.2f}, вероятность обслуживания: {p_accept:.2f}, средняя длина очереди: {avg}')
    p_reject, p_accept, lq = system.get_theoretical()
    print(f'Вероятность отказа: {p_reject:.2f}, вероятность обслуживания: {p_accept:.2f}, '
          f'средняя длина очереди: {lq:.4f}')

