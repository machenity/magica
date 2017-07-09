import sys

if sys.version_info[0] < 3:
    sys.exit('Magica requires version 3')

from setuptools import setup, find_packages

setup(
    name='magica',
    version='0.1',
    description='도서 검색·메모·구입하는 터미널 기반 툴',
    author='machenity',
    author_email='machenity@gmail.com',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'tinydb',
    ],
    url='https://github.com/machenity/magica',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3'
)