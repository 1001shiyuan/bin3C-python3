"""Python 3 port of bin3C for use by METAHICT."""

import numpy as _np

# The upstream 0.1.1 code uses aliases removed in NumPy 1.24.  Keep the
# compatibility shim here so every submodule sees the same Python 3 runtime.
for _name, _value in (("int", int), ("float", float), ("bool", bool)):
    if _name not in _np.__dict__:
        setattr(_np, _name, _value)

__version__ = "0.1.1.post1"
