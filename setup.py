from setuptools import setup, find_packages

setup(
    name='GameOfLife',
    version='0.1.0',
    description='A Conway\'s Game of Life simulation using Pygame',
    author='Richard Morris',
    author_email='richard.morris@anu.edu.au',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pygame>=2.0.0',
    ],
    entry_points={
        'console_scripts': [
            'life_app=GameOfLife.main:main',
        ],
    },
)
