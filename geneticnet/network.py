import numpy as np
import random

from geneticnet.block import Block
from geneticnet.connection import Connection

class Network:
    def __init__(self, input_vectors: list, ground_truth_labels: list):
        self.input_vectors = input_vectors
        self.input_size = len(input_vectors[0])
        self.ground_truth_labels = ground_truth_labels
        self.output_classes = list(set(ground_truth_labels))
        self.input_blocks = []
        self.middle_blocks = []
        self.output_blocks = []
        self.add_output_blocks()
        self.add_input_blocks()

    def add_output_blocks(self):
        self.output_blocks = [Block(depth=1, output_class=output_class) for output_class in self.output_classes]

    def add_input_blocks(self):
        self.input_blocks = [Block(depth=0) for _ in range(self.input_size)]

    def get_allowed_next_block(self, selected_block):
        allowed_blocks = {block for block in (self.output_blocks + self.middle_blocks) if block.depth > selected_block.depth}
        return random.sample(allowed_blocks, 1)[0]

    def get_allowed_previous_block(self, selected_block):
        allowed_blocks = {block for block in (self.input_blocks + self.middle_blocks) if block.depth < selected_block.depth}
        return random.sample(allowed_blocks, 1)[0]

    def add_random_connection(self):
        allowed_blocks = (self.input_blocks + self.middle_blocks)
        selected_block = random.sample(allowed_blocks, 1)[0]
        selected_next_block = self.get_allowed_next_block(selected_block)
        connection = Connection(selected_next_block, np.random.normal(0, 0.1))
        # selected_block.connections.append(connection)
        selected_block.add_connection(connection)

    def add_random_block(self):
        block = Block(depth=random.random())
        selected_previous_block = self.get_allowed_previous_block(block)
        selected_next_block = self.get_allowed_next_block(block)
        connection_previous = Connection(block, np.random.normal(0, 0.1))
        connection_next = Connection(selected_next_block, np.random.normal(0, 0.1))
        selected_previous_block.add_connection(connection_previous)
        block.add_connection(connection_next)
        self.middle_blocks.append(block)

    def reset_network_values(self):
        for block in (self.input_blocks + self.middle_blocks + self.output_blocks):
            block.value = 0

    def activate_next(self, block):
        for connection in block.connections:
            connected_block = connection.block
            connected_block.value += block.value * connection.activation

    def run(self, input_vector):
        self.reset_network_values()
        for index, input in enumerate(input_vector):

            block = self.input_blocks[index]
            block.value += input
            self.activate_next(block)

        for block in sorted(self.middle_blocks, key=lambda block: block.depth):
            self.activate_next(block)

        min_value = min([output.value for output in self.output_blocks])
        if min_value < 0:
            for output in self.output_blocks:
                output.value -= min_value
        total_value = sum([output.value for output in self.output_blocks])
        if total_value <= 0:
            total_value = 1
        results = {output.output_class: output.value / total_value for output in self.output_blocks}
        return results

    def get_batch_loss(self, input_vectors=None, ground_truths=None):
        if input_vectors is None:
            input_vectors = self.input_vectors
        if ground_truths is None:
            ground_truths = self.ground_truth_labels
        if len(input_vectors) != len(ground_truths):
            raise Exception('The length of the input vectors must match the length of the ground truth labels.')
        losses = []
        for input_vector, ground_truth in zip(input_vectors, ground_truths):
            result = self.run(input_vector)
            ground_truth_prediction = result[ground_truth]
            loss = 1 - ground_truth_prediction
            losses.append(loss)
        return sum(losses) / len(losses)
