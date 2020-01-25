import random
import math

from geneticnet.trainer import Trainer

def test_trainer():
    inputs = [
        [0, .000001],
        [0, 1],
        [0, -2],
        [-1, 0],
        [1, 1],
        [3, -5],
        [2, 2],
        [-5, 6]
    ]
    ground_truths = [
        'pos',
        'pos',
        'neg',
        'neg',
        'pos',
        'neg',
        'pos',
        'pos'
    ]
    trainer = Trainer(inputs, ground_truths, population_size=100, generation_count=20, initial_random_block_count=3)
    result = trainer.train()
    assert result['loss'] == 0


def test_trainer_complex():
    inputs = []
    for _ in range(100):
        input = [random.random() * 10, random.random(), random.randint(0, 20)]
        inputs.append(input)

    def hidden_function(input):
        a, b, c = input
        value = (a * b) - c
        if value > 0:
            return 'pos'
        else:
            return 'neg'

    ground_truths = [hidden_function(input) for input in inputs]

    trainer = Trainer(inputs, ground_truths, population_size=100, generation_count=20, initial_random_block_count=10)
    result = trainer.train()
    assert result['loss'] == 0
