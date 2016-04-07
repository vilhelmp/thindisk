#!/usr/bin/env python

from setuptools import setup

setup(
    name='ThinDisk',
    version='0.0.0',
    summary='Sebastien Marets Python thin disk model '
            'from https://github.com/smaret/thindisk',
    entry_points = {
        'console_scripts': [
            'thindiskpy = src.thindisk:main'
        ]
    },

)
