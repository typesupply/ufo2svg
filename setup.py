#!/usr/bin/env python

import sys
from setuptools import setup

try:
    import fontTools
except:
    print("*** Warning: ufo2svg requires FontTools, see:")
    print("    fonttools.sf.net")


setup(name="ufo2svg",
    version="0.1",
    description="Convert a UFO to a SVG font format file.",
    author="Tal Leming",
    author_email="tal@typesupply.com",
    url="https://github.com/typesupply/ufo2svg",
    license="MIT",
    packages=[
        "ufo2svg"
    ],
    package_dir={"":"Lib"}
)
