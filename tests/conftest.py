##############################################################################
# MDTraj: A Python Library for Loading, Saving, and Manipulating
#         Molecular Dynamics Trajectories.
# Copyright 2012-2017 Stanford University and the Authors
#
# Authors: Matthew Harrigan
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

import os

import pytest

flaky_pdb_dl = pytest.mark.flaky(rerun=3, reason='github-node flaky pdb dl')


@pytest.fixture(scope="session")
def get_fn():
    test_dir = os.path.dirname(os.path.abspath(__file__))

    def _get_fn(fn):
        return f"{test_dir}/data/{fn}"

    return _get_fn
