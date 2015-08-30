import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    description = f.read()

packages = [
    'movienamer'
]

setup(
    name='movienamer',
    version=__import__('movienamer').__version__,
    author='Divij Bindlish',
    author_email='dvjbndlsh93@gmail.com',
    description='Command-line utility to organize movies',
    license='MIT',
    long_description=description,
    url='https://github.com/divijbindlish/movienamer',
    install_requires=required,
    packages=packages,
    entry_points={
        'console_scripts': ['movienamer = movienamer.main:main']
    }
)
