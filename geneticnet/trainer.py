from operator import itemgetter

from geneticnet.network import Network

class Trainer:
    def __init__(self, input_vectors,
                 ground_truth_labels,
                 population_size=100,
                 generation_count=10,
                 initial_random_block_count=3,
                 initial_random_connection_count=10):
        self.input_vectors = input_vectors
        self.ground_truth_labels = ground_truth_labels
        self.population_size = population_size
        self.generation_count = generation_count
        self.initial_random_connection_count = initial_random_connection_count
        self.initial_random_block_count = initial_random_block_count
        self.population = []

    def create_network(self):
        network = Network(input_vectors=self.input_vectors, ground_truth_labels=self.ground_truth_labels)
        for _ in range(self.initial_random_block_count):
            network.add_random_block()
        for _ in range(self.initial_random_connection_count):
            network.add_random_connection()
        return {'network': network, 'loss': None}

    def train(self):
        for _ in range(self.population_size):
            self.population.append(self.create_network())

        for _ in range(self.generation_count):
            for network_dict in self.population:
                network = network_dict['network']
                loss = network.get_batch_loss()
                network_dict['loss'] = loss
            self.population = sorted(self.population, key=itemgetter('loss'))
            self.population = self.population[:20]
            while len(self.population) < self.population_size:
                self.population.append(self.create_network())
        return self.population[0]

