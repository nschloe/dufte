import warnings

from .main import legend, show_bar_values, style, style_bar, ylabel

__all__ = ["legend", "style", "style_bar", "ylabel", "show_bar_values"]

warnings.warn(
    "dufte has been merged into mplx, <https://github.com/nschloe/mplx>",
    DeprecationWarning,
)
