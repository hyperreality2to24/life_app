from setuptools import setup, find_packages

setup(
    name='GameOfLife',
    version='0.1.0',
    description='A Conway\'s Game of Life simulation using Pygame',
    author='Your Name',
    author_email='your.email@example.com',
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
