# numbapy

`numbapy` is a minimal example package showing how to use **Numba** to JIT-compile a simple function.

## Install

```bash
pip install numbapy
```

(For development, use `pip install -e .[dev,docs,demo]`.)

## Quickstart

```python
import numpy as np
from numbapy import sum_of_squares

x = np.arange(100_000, dtype=np.float64)
print(sum_of_squares(x))
```
