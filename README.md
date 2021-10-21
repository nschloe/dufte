<p align="center">
  <a href="https://github.com/nschloe/dufte"><img alt="dufte-logo" src="https://nschloe.github.io/dufte/logo.svg" width="40%"></a>
  <p align="center"><a href="https://en.wikipedia.org/wiki/Berlin_German">Da kiekste, wa?</a></p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/dufte.svg?style=flat-square)](https://pypi.org/project/dufte/)
[![Anaconda Cloud](https://anaconda.org/conda-forge/dufte/badges/version.svg?=style=flat-square)](https://anaconda.org/conda-forge/dufte/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dufte.svg?style=flat-square)](https://pypi.org/project/dufte/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/dufte.svg?logo=github&label=Stars&logoColor=white&style=flat-square)](https://github.com/nschloe/dufte)
[![PyPi downloads](https://img.shields.io/pypi/dm/dufte.svg?style=flat-square)](https://pypistats.org/packages/dufte)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/dufte/ci?style=flat-square)](https://github.com/nschloe/dufte/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/dufte.svg?style=flat-square)](https://codecov.io/gh/nschloe/dufte)
[![LGTM](https://img.shields.io/lgtm/grade/python/github/nschloe/dufte.svg?style=flat-square)](https://lgtm.com/projects/g/nschloe/dufte)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

This package creates clean and beautiful plots that work on light and dark backgrounds.
Inspired by the work of [Edward Tufte](https://en.wikipedia.org/wiki/Edward_Tufte).

To use, simply select the `dufte` style:

```python
import dufte
import matplotlib.pyplot as plt

# global setting:
plt.style.use(dufte.style)

# with a context manager:
with plt.style.context(dufte.style_bar):
    # ...
    pass
```

Check out `dufte.legend()`, `dufte.ylabel()`, and `dufte.show_bar_values()` for more
duftiness.

#### Comparison with default Matplotlib

See [here](tests/create_comparison.py) for how to create the below plots.

<a href="tests/create_comparison.py">
<table width="100%">
  <tr>
  <td width="50%"><img src="https://nschloe.github.io/dufte/ex1-mpl.svg"/></td>
  <td width="50%"><img src="https://nschloe.github.io/dufte/ex1-dufte.svg"/></td>
  </tr>
  <tr>
    <td>matplotlib</td>
    <td>dufte with <code>dufte.legend()</code></td>
  </tr>
</table>
</a>

<a href="tests/create_comparison.py">
<table width="100%">
  <tr>
  <td width="33%"><img src="https://nschloe.github.io/dufte/bars-mpl.svg"/></td>
  <td width="33%"><img src="https://nschloe.github.io/dufte/bars-dufte1.svg"/></td>
  <td width="33%"><img src="https://nschloe.github.io/dufte/bars-dufte2.svg"/></td>
  </tr>
  <tr>
    <td>matplotlib</td>
    <td>dufte</td>
    <td>dufte with <code>dufte.show_bar_values()</code></td>
  </tr>
</table>
</a>

Further reading:

- [Remove to improve: data-ink ratio](https://www.darkhorseanalytics.com/blog/data-looks-better-naked)

  <img src="https://nschloe.github.io/dufte/data-ink.webp" width="50%"/>

- [Remove to improve: Line Graph Edition](https://youtu.be/bDbJBWvonVI)
- [Show the Data - Maximize the Data Ink Ratio](https://youtu.be/pCp0a5_YIWE)
- [Randal S. Olson's blog entry](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
- [prettyplotlib](https://github.com/olgabot/prettyplotlib)
- [Wikipedia: Chartjunk](https://en.wikipedia.org/wiki/Chartjunk)

Projects using dufte:

- [perfplot](https://github.com/nschloe/perfplot)
- [stargraph](https://github.com/nschloe/stargraph)

### Background

[![xdoc](https://img.shields.io/badge/Rendered%20with-xdoc-f2eecb?style=flat-square)](https://chrome.google.com/webstore/detail/xdoc/anidddebgkllnnnnjfkmjcaallemhjee)

The position $`x_i`$ of the line annotations is computed as the solution of a
non-negative least-squares problem

```math
\begin{align}
\frac{1}{2}\sum_i (x_i - t_i)^2 \to \min_x,\\
(x_i - x_j)^2 \ge a^2 \quad \forall i,j.
\end{align}
```

where $`a`$ is the minimum distance between two entries and $`t_i`$ is the target
position.

### Testing

To run the dufte unit tests, check out this repository and type

```
pytest
```

### Other style sheets and further reading

- [John Garrett, _Science Plots_](https://github.com/garrettj403/SciencePlots)
- [Dominik Haitz, _Cyberpunk style_](https://github.com/dhaitz/mplcyberpunk)
- [Dominik Haitz, _Matplotlib stylesheets_](https://github.com/dhaitz/matplotlib-stylesheets)
- [Carlos da Costa, _The Grand Budapest Hotel_](https://github.com/cako/mpl_grandbudapest)
- [Danny Antaki, _vaporwave aesthetics_](https://github.com/dantaki/vapeplot)
- [QuantumBlack Labs, _QuantumBlack_](https://github.com/quantumblacklabs/qbstyles)
