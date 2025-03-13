from Lab4.numgen import GammaGenerator
from Lab4.generator import TrigonomicOperations, Generator

class Customer:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time

class PureQueue:
    def __init__(self, limit):
        self.limit = limit
        self.customers = []
        self.current_time = 0

    def is_full(self):
        return len(self.customers) >= self.limit

    def add_customer(self, customer):
        if not self.is_full():
            self.customers.append(customer)
            print(f"Клиент пришел в очередь в {customer.arrival_time:.2f}, очередь: {len(self.customers)}")
            return True
        else:
            print("Очередь полна, клиент уходит.")
            return False

    def serve_customer(self, gen):
        if self.customers:
            customer = self.customers.pop(0)
            service_duration = gen
            print(f"Клиент обслуживается, время обслуживания {service_duration:.2f}, очередь: {len(self.customers)}")
            return service_duration
        return 0

class LimitedSingleServer:
    def __init__(self, queue_limit, generator, service_time, arrival_time):
        self.queue_limit = queue_limit
        self.generator = generator
        self.rejected = 0
        self.accepted = 0
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.is_free = True

    def simulate_system(self, total_time):
        queue = PureQueue(self.queue_limit)
        current_time = 0
        next_arrival_time = self.generator.generate(1)[0] if self.generator is not None else self.arrival_time

        while current_time < total_time:
            if next_arrival_time < current_time:
                customer = Customer(next_arrival_time)
                if not queue.add_customer(customer):
                    self.rejected += 1
                next_arrival_time += self.generator.generate(1)[0] if self.generator is not None else self.arrival_time
            else:
                service_duration = queue.serve_customer(self.generator.generate(1)[0] if self.generator is not None else self.service_time)
                if service_duration > 0:
                    self.accepted += 1
                    current_time += service_duration
                else:
                    current_time += self.arrival_time

    def get_values(self):
        total_clients = self.accepted + self.rejected
        if total_clients == 0:
            return 0, 0
        p_rejection = self.rejected / total_clients
        p_served = self.accepted / total_clients
        return p_rejection, p_served

    def get_theoretical(self):
        mu = 1 / self.service_time
        l = self.arrival_time
        po = l / mu
        p0 = (1 - po) / (1 - po ** (self.queue_limit + 2)) if po != 1 else 1 / (self.queue_limit + 2)
        p_reject =  p0 * po ** (self.queue_limit + 1)
        p_accept = 1 - p_reject
        a = l * p_accept

        loc = ((po ** 2 * (1 - po ** self.queue_limit * (self.queue_limit - self.queue_limit * po + 1)))
               / (1 - po) ** 2) if po != 1 else (self.queue_limit * (self.queue_limit + 1)) / (2 * (self.queue_limit + 2))
        toc = loc / l
        lcmo = 1 + loc
        tcmo = lcmo / l if po != 1 else (self.queue_limit + 1) / (2 * mu)
        return p_reject, p_accept, lcmo, tcmo

if __name__ == "__main__":
    lambda_value = 0.7
    limit = 3
    service_time = 1.25
    max_time = 3000
    oper = TrigonomicOperations(10, -1)
    generator = Generator(oper)
    gg = GammaGenerator(1 / lambda_value)
    server = LimitedSingleServer(limit, generator, service_time, lambda_value)
    server.simulate_system(max_time)
    p_reject, p_accept = server.get_values()
    print(f'Вероятность отказа: {p_reject:.2f}, вероятность обслуживания: {p_accept:.2f}')
    p_reject, p_accept, lcmo, tcmo = server.get_theoretical()
    print(f'Вероятность отказа: {p_reject:.2f}, вероятность обслуживания: {p_accept:.2f}, '
          f'среднее число заявок: {lcmo:.2f}, среднее время нахождения заявки: {tcmo:.2f}')
