from packaging.version import Version
import numpy as np


if Version(np.__version__) >= Version('2'):
    np._set_promotion_state("weak_and_warn")
