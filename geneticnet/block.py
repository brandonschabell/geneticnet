import random

class Block:
    def __init__(self, depth: float, output_class=None):
        self.depth = depth
        self.connections = []
        self.output_class = output_class
        self.value = 0

    def add_connection(self, connection):
        self.connections.append(connection)

    def remove_connection(self):
        self.connections.remove(random.sample(self.connections, 1)[0])
