from .core import sum_of_squares

try:
	from ._version import __version__
except Exception:  # pragma: no cover
	__version__ = "0.0.0"

__all__ = ["sum_of_squares", "__version__"]
