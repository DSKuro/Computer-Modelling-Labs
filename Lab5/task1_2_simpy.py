import simpy
from Lab4.numgen import GammaGenerator
from Lab4.generator import TrigonomicOperations, Generator

class System:
    def __init__(self, env, capacity, generator, num_serv, service_time):
        self.env = env
        self.queue = simpy.Store(env)
        self.capacity = capacity
        self.server = simpy.Resource(env, capacity=num_serv)
        self.accepted = 0
        self.rejected = 0
        self.generator = generator
        self.queue_length = []
        self.service_time = 0
        self.service_time = service_time
        self.time = 0

    def arrive(self, customer_id):
        self.queue_length.append(len(self.queue.items) * (self.env.now - self.time))
        self.time = self.env.now
        if self.capacity is None or len(self.queue.items) < self.capacity:
            self.queue.put(customer_id)
            print(f'Клиент {customer_id} зашёл в очередь в {self.env.now:.2f}')
            self.accepted += 1
            yield self.env.process(self.service(customer_id))
        else:
            print(f'Клиент {customer_id} ушёл, очередь полная в {self.env.now:.2f}')
            self.rejected += 1

    def service(self, customer_id):
        with self.server.request() as request:
            yield request
            print(f'Клиент {customer_id} начинает обслуживание в {self.env.now:.2f}')
            yield self.env.timeout(self.generator.generate(1)[0] if self.generator is not None else self.service_time)
            print(f'Клиент {customer_id} закончил обслуживание в {self.env.now:.2f}')

            self.queue.items.pop()

    def get_values(self):
        total_clients = self.accepted + self.rejected
        if total_clients == 0:
            return 0, 0
        p_rejection = self.rejected / total_clients
        p_served = self.accepted / total_clients
        avg_len = sum(self.queue_length) / len(self.queue_length)
        return p_rejection, p_served, avg_len

def customer_generator(env, system, gen, arrival_time):
    customer_id = 0
    while True:
        yield env.timeout(gen.generate(1)[0] if gen is not None else arrival_time)
        customer_id += 1
        env.process(system.arrive(customer_id))

if __name__ == "__main__":
    env = simpy.Environment()
    system_capacity = 3
    arrival_rate = 0.7
    gg = GammaGenerator(1 / arrival_rate)

    oper = TrigonomicOperations(10, -1)
    generator = Generator(oper)

    system = System(env, system_capacity, generator, 5, service_time= 1.25)
    env.process(customer_generator(env, system, generator, arrival_rate))
    env.run(until=3000)

    p_reject, p_accept, avg = system.get_values()
    print(f'Вероятность отказа: {p_reject:.2f}, вероятность обслуживания: {p_accept:.2f}, средняя длина очереди: {avg}')