# /usr/bin/env python
from os import path
from setuptools import setup


with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(
    name='pixelmap',
    version='1.0',
    description='Map of cool pixel data structures',
    long_description=long_description,
    author='Alfredo Yebra Jr.',
    author_email='f@gmail.com',
    license='MIT',
    url='https://github.com/yebra06/pixelmap',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    packages=['pixelmap'],
)
