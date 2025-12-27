.. image:: https://travis-ci.org/nist-ionstorage/electrode.svg?branch=master
  :target: https://travis-ci.org/nist-ionstorage/electrode

.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.10118.png
  :target: https://zenodo.org/record/10118


Description
===========

Electrode is a toolkit to develop and analyze RF ion traps. It can
optimize 2D surface electrode patterns to achieve desired trapping
properties and extract relevant parameters of the resulting geometry.
The software also treats precomputed 3D volumetric field and potential
data transparently.

Quick overview and tutorial:
http://nbviewer.ipython.org/github/nist-ionstorage/electrode/blob/master/examples/tutorial.ipynb

See also:

[1] Roman Schmied <roman.schmied@unibas.ch>, SurfacePattern software
package.
http://atom.physik.unibas.ch/people/romanschmied/code/SurfacePattern.php

[2] Roman Schmied: Electrostatics of gapped and finite surface
electrodes. New Journal of Physics 12:023038 (2010).
http://dx.doi.org/10.1088/1367-2630/12/2/023038

[3] Roman Schmied, Janus H. Wesenberg, and Dietrich Leibfried: Optimal
Surface-Electrode Trap Lattices for Quantum Simulation with Trapped
Ions. Physical Review Letters 102:233002 (2009).
http://dx.doi.org/10.1103/PhysRevLett.102.233002

[4] A. van Oosterom and J. Strackee: The Solid Angle of a Plane
Triangle, IEEE Transactions on Biomedical Engineering, vol. BME-30, no.
2, pp. 125-126. (1983)
http://dx.doi.org/10.1109/TBME.1983.325207

[5] Mário H. Oliveira and José A. Miranda: Biot–Savart-like law in
electrostatics. European Journal of Physics 22:31 (2001).
http://dx.doi.org/10.1088/0143-0807/22/1/304



Dependencies
============

Debian based GNU/Linuxes
------------------------

    # apt-get install python-cvxopt python-numpy python-matplotlib \
                      python-scipy python-traits python-shapely

to use the ipython based notebooks, try

    # apt-get install ipython-notebook


Usage
=====

Running console scripts
-----------------------

The tutorial contains two examples of surface electrode traps (five_wire
and threefold). The relevant code can be all pasted into a Python script
(five_wire.py) or IPython notebook (see below) and executed.

Without installing anything
...........................

Use e.g.:

    $ PYTHONPATH=. python your_script.py

to run a script without installing the `electrode` package.

Installation
============

Using pip (recommended)
------------------------

For modern Python and pip (PEP 517 build), install from the project root:

    $ python -m pip install .

To install in editable/development mode so changes in this directory take
effect immediately:

    $ python -m pip install -e .

Notes:

- This project provides a `pyproject.toml` so pip can install build-time
  dependencies (Cython, numpy) required to build the C extension.
- Building the optional C extension (`electrode._transformations`) requires
  a working C compiler and the development headers for Python and NumPy.

Legacy setup.py commands
------------------------

If you prefer the legacy setuptools workflow you can still use:

    $ python setup.py develop

or

    $ python setup.py install

but the `pip` workflow above is recommended for reproducible builds.


Runing the notebooks
....................

Ensure you have ipython > 0.11 with ipython notebook installed, then run

    $ ipython notebook --pylab=inline --notebook-dir=examples --script
