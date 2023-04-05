#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages


setup(
    name="litehbm",
    description="High Bandwidth Memory BIOS and testing code",
    author="Grant Goates",
    author_email="ggoates17@gmail.com",
    url="http://github.com/capstone2022team17/drgbl/",
    download_url="https://github.com/capstone2022team17/litehbm",
    license="BSD",
    python_requires="~=3.6",
    packages=find_packages(exclude=("test*", "sim*", "doc*", "examples*")),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "litehbm_gen=litehbm.gen:main",
        ],
    },
)