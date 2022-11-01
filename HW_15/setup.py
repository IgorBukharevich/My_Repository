"""
A setuptools base setup module
"""
from os import path
from setuptools import setup
from setuptools import find_namespace_packages

PATH = path.abspath(path.dirname(__file__))
# read file
with open(path.join(PATH, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='My_packages',
    version='1.0',
    long_description=long_description,
    long_description_content_type= 'text/markdown',
    url='https://github.com/IgorBukharevich/My_Repository',
    author='IgorBukharevich',
    author_email='igor.bukharevich.lifanor@gmail.com',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    python_requires='>= 3.6, >4',
    install_requires=[
        'flask',
        'prettytable'
    ],
)