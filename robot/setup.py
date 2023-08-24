from setuptools import setup

setup(
    name='robot',
    version='0.1',
    description='Library for controlling the robot',
    packages=['robot'],
    install_requires=[
        'RPi.GPIO',
        # List any other required dependencies here
    ],
)
