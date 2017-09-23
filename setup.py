"""An extensible wrapper for the SEPTA API.

See:
http://www3.septa.org
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='septa',
    version='0.1.0a1',
    description='An extensible wrapper for the SEPTA API',
    long_description=long_description,
    url='https://github.com/snood1205/septa',
    author='Eli Sadoff',
    author_email='snood1205@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    extras_require={
        'dev': [],
        'test': []
    }
)
