from setuptools import setup, find_packages
import os


def open_file(fname):
    """helper function to open a local file"""
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name='moviesearch',
    version='0.0.2',
    author='Malte Bonart',
    author_email='malte@spiced-academy.com',
    packages=find_packages(),
    url='https://github.com/bonartm/moviesearch',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    description='Moviesearch is a Python library for searching for movies',
    long_description=open_file('README.md').read(),
    # end-user dependencies for your library
    install_requires=[
        'pandas',
        'scikit-learn',
        'fuzzywuzzy',
        'python-Levenshtein'
    ],
    # include additional data
    package_data={
        'moviesearch': ['data/*.csv']
    }
)
