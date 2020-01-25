import os
from setuptools import setup, find_packages

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


test_requirements = [
    'pytest'
]

setup(
    name='geneticnet',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/brandonschabell/geneticnet',
    download_url='https://github.com/brandonschabell/geneticnet/archive/v0.0.1.tar.gz',
    license='MIT',
    author='Brandon Schabell',
    author_email='brandonschabell@gmail.com',
    description='A graph-like network that is both built and tuned via a genetic algorithm.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='~=3.7',
    install_requires=[
        'geneticpy',
        'tqdm',
        'Pillow',
        'numpy'
    ],
    tests_require=test_requirements,
    setup_requires=[
        'pytest-runner'
    ],
    extras_require={
      'tests': test_requirements
    },
)
