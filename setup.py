import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

packages = [
    'movienamer'
]

setup(
    name='movienamer',
    version='0.0.1',
    author='Divij Bindlish',
    author_email='me@divijbindlish.com',
    description='Command-line utility to properly organize movies',
    url='https://github.com/divijbindlish/movienamer',
    install_requires=required,
    packages=packages,
    entry_points={
        'console_scripts': ['movienamer = movienamer.main:main']
    }
)
