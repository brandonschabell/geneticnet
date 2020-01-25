import numpy as np
import os
from PIL import Image
import shutil

from geneticnet.network import Network
from tests.utilities import get_testfiles_path

def test_create_network():
    input_vector = [1, 2, 3]
    network = Network(input_size=3, output_classes=['even', 'odd'])
    result = network.run(input_vector)
    print(result)



