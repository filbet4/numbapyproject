# numbapy

A tiny “hello-world” Python package that demonstrates using **Numba** to speed up a simple computation.

## Install

From source (recommended while developing):

```bash
pip install -e .[dev,docs,demo]
```

## Quick demo

```python
import numpy as np
from numbapy import sum_of_squares

x = np.arange(10_000, dtype=np.float64)
print(sum_of_squares(x))
```

## Docs

The docs are built with MkDocs and deployed to GitHub Pages via Actions.

## Releases

On release/tag, a GitHub Actions workflow builds the package and publishes to **TestPyPI**.

## Binder / Colab

See the demo notebook: `notebooks/demo.ipynb`.
- Binder: `https://mybinder.org/v2/gh/filbet4/numbapyproject/HEAD?labpath=notebooks%2Fdemo.ipynb`
- Colab: open the notebook in Colab and run the install cell.
