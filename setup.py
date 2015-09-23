#from distutils.core import setup
from setuptools import setup

setup(
    name='CityTraderPythonLib',
    version='0.1',
    install_requires=[
        "requests",
        "requests[security]",
        "oauth",
    ],
    packages=['citytrader',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
