##############################################################################
# MDTraj: A Python Library for Loading, Saving, and Manipulating
#         Molecular Dynamics Trajectories.
# Copyright 2012-2013 Stanford University and the Authors
#
# Authors: Robert McGibbon
# Contributors:
#
# MDTraj is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with MDTraj. If not, see <http://www.gnu.org/licenses/>.
##############################################################################

"""
Code to delay the import of a moldule, and give a nice error message if
the module is not installed. for dealing with dependencies.
"""
##############################################################################
# imports
##############################################################################

import importlib
import inspect
import os
import sys
import textwrap

__all__ = ["import_"]

##############################################################################
# globals
##############################################################################

MESSAGES = {
    "networkx": """
    The code at {filename}:{line_number} requires the python module
    NetworkX, which is a software package for the creation, manipulation, and study of
    the structure, dynamics, and functions of complex networks.

    NetworkX can be downloaded from https://pypi.python.org/pypi/networkx/, or
    installed with the python "easy_install" or "pip" package managers using:

    # easy_install networkx
    or
    # pip install networkx
    """,
    "tables": """
    The code at {filename}:{line_number} requires the python module PyTables,
    which is a package for managing hierarchical datasets and designed to
    efficiently and easily cope with extremely large amounts of data.

    PyTables can be downloaded from http://www.pytables.org, or installed with
    the python "easy_install" or "pip" package managers using:

    # easy_install tables
    or
    # pip install tables

    PyTables also depends on the numexpr package, as well as the C-language
    HDF5 library. For detailed installation instructions, visit
    http://pytables.github.io/usersguide/installation.html
    """,
    "netCDF4": """
    The code at {filename}:{line_number} requires the netcdf4-python module,
    which is a python interface to the NetCDF software libraries and self-describing,
    machine-independent data formats that support the creation, access, and
    sharing of array-oriented scientific data.

    netcdf4-python can be downloaded from https://pypi.python.org/pypi/netCDF4,
    or installed with the python "conda" or "pip" package managers using:

    # conda install -c conda-forge netCDF4
    or
    # pip install netCDF4

    netcdf4-python also depends on the C-language HDF5 and NetCDF libraries.
    For detailed installation instructions, visit
    https://unidata.github.io/netcdf4-python/#quick-install
    """,
    "openmm.unit": """
    The code at {filename}:{line_number} requires the openmm.unit module,
    which is a python package for unit conversion.

    openmm.unit is installed with OpenMM >= 7.6, which is available at  http://openmm.org
    It can be installed with the "conda" package mangers using:

    conda install -c conda-forge openmm
    """,
    "openmm.app": """
    The code at {filename}:{line_number} requires the openmm.app module, which is
    the python OpenMM application layer. OpenMM is a toolkit for molecular simulation
    using high performance GPU code.

    openmm.app is installed with OpenMM >= 7.6, which is available at http://openmm.org
    """,
    "pandas": """
    The code at {filename}:{line_number} requires the "pandas" package, which is
    an open source, BSD-licensed library providing high-performance, easy-to-use
    data structures and data analysis tools for the Python programming language.

    pandas can be downloaded from https://pypi.python.org/pypi/pandas or installed
    with the python "easy_install" or "pip" package managers using:

    # easy_install pandas
    or
    # pip install pandas
    """,
}


##############################################################################
# functions
##############################################################################


def import_(module):
    """Import a module, and issue a nice message to stderr if the module isn't installed.

    Currently, this function will print nice error messages for networkx,
    tables, netCDF4, and openmm.unit, which are optional MDTraj dependencies.

    Parameters
    ----------
    module : str
        The module you'd like to import, as a string

    Returns
    -------
    module : {module, object}
        The module object

    Examples
    --------
    >>> # the following two lines are equivalent. the difference is that the
    >>> # second will check for an ImportError and print you a very nice
    >>> # user-facing message about what's wrong (where you can install the
    >>> # module from, etc) if the import fails
    >>> import tables
    >>> tables = import_('tables')
    """
    try:
        return importlib.import_module(module)
    except ImportError:
        try:
            message = MESSAGES[module]
        except KeyError:
            message = "The code at {filename}:{line_number} requires the " + module + " package"

        frame, filename, line_number, function_name, lines, index = inspect.getouterframes(inspect.currentframe())[1]

        m = message.format(filename=os.path.basename(filename), line_number=line_number)
        m = textwrap.dedent(m)

        bar = "\033[91m" + "#" * max(len(line) for line in m.split(os.linesep)) + "\033[0m"

        print("", file=sys.stderr)
        print(bar, file=sys.stderr)
        print(m, file=sys.stderr)
        print(bar, file=sys.stderr)
        raise ImportError(m)
