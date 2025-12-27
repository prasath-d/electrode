#!/usr/bin/python
# -*- coding: utf8 -*-
#
#   electrode: numeric tools for Paul traps
#
#   Copyright (C) 2011-2012 Robert Jordens <jordens@phys.ethz.ch>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

#from __future__ import (absolute_import, print_function,
#       unicode_literals, division)

from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
from glob import glob
import numpy
import io
import os

# read long description from README if present
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
long_description = ''
if os.path.exists(readme_path):
    with io.open(readme_path, encoding='utf8') as f:
        long_description = f.read()

setup(
        name = "electrode",
        version = "1.5+dev",
        author = "Robert Jordens",
        author_email = "jordens@gmail.com",
        url = "http://github.com/nist-ionstorage/electrode",
        description = "toolkit to develop and analyze rf surface ion traps",
        license = "GPLv3+",
        python_requires = ">=3.6",
        long_description = long_description,
        long_description_content_type = 'text/x-rst',
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ],
        install_requires = [
            "numpy", "scipy", "nose", "cython", "sphinx",
            "numpydoc"],
        extras_require = {
            "notebooks": ["ipython>=0.12"],
            "integrate": ["qc"],
            "optimization": ["cvxopt>=1"],
            "visualization": ["mayavi>4", "matplotlib"],
            "polygons": ["shapely>=1.2"],
            "gds": ["gdsii"],
            },
        dependency_links = [],
        packages = find_packages(),
        namespace_packages = [],
        #test_suite = "electrode.tests.test_all",
        test_suite = "nose.collector",
        include_package_data = True,
        ext_modules=[
                Extension("electrode._transformations",
                    sources=["electrode/transformations.c"],
                    include_dirs=[numpy.get_include()]),
                Extension("electrode.cexpressions",
                    sources=["electrode/cexpressions.pyx",
                         #"electrode/cexpressions.c",
                         ],
                    extra_compile_args=[
                        "-ffast-math", # improves expressions
                        #"-Wa,-adhlns=cexprssions.lst", # for amusement
                        ],
                    include_dirs=[numpy.get_include()]),
            ],
        cmdclass = {"build_ext": build_ext},
        )
