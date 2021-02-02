<p align="center">
  <a href="https://github.com/nschloe/dufte"><img alt="dufte-logo" src="https://nschloe.github.io/dufte/logo.svg" width="40%"></a>
  <p align="center"><a href="https://en.wikipedia.org/wiki/Edward_Tufte">Tufte</a>-style plots <a href="https://www.linguee.com/german-english/translation/dufte.html">from Berlin</a>.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/dufte.svg?style=flat-square)](https://pypi.org/project/dufte)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dufte.svg?style=flat-square)](https://pypi.org/pypi/dufte/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/dufte.svg?logo=github&label=Stars&logoColor=white&style=flat-square)](https://github.com/nschloe/dufte)
[![PyPi downloads](https://img.shields.io/pypi/dm/dufte.svg?style=flat-square)](https://pypistats.org/packages/dufte)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/dufte/ci?style=flat-square)](https://github.com/nschloe/dufte/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/dufte.svg?style=flat-square)](https://codecov.io/gh/nschloe/dufte)
[![LGTM](https://img.shields.io/lgtm/grade/python/github/nschloe/dufte.svg?style=flat-square)](https://lgtm.com/projects/g/nschloe/dufte)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

This package creates clean and beautiful plots that work on light and dark backgrounds.

<img src="https://nschloe.github.io/dufte/ex1-light.svg"> |  <img src="https://nschloe.github.io/dufte/ex1-dark.svg">
:----:|:----:|

Simply select the `dufte` style and, if desired, call `dufte.legend()` to get
line annotations on the right.
```python
import matplotlib.pyplot as plt
import dufte
import numpy

plt.style.use(dufte.style)

numpy.random.seed(0)

x0 = numpy.linspace(0.0, 3.0, 100)
y0 = x0 / (x0 + 1)
y0 += 0.1 * numpy.random.rand(len(y0))
plt.plot(x0, y0, label="no balacing")

x1 = numpy.linspace(0.0, 3.0, 100)
y1 = 1.5 * x1 / (x1 + 1)
y1 += 0.1 * numpy.random.rand(len(y1))
plt.plot(x1, y1, label="CRV-27")

x2 = numpy.linspace(0.0, 3.0, 100)
y2 = 1.6 * x2 / (x2 + 1)
y2 += 0.1 * numpy.random.rand(len(y2))
plt.plot(x2, y2, label="CRV-27*")

dufte.legend()

plt.show()
```
Further reading:

 * [Randal S. Olson's blog entry](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
 * [prettyplotlib](https://github.com/olgabot/prettyplotlib)
 * [Wikipedia: Chartjunk](https://en.wikipedia.org/wiki/Chartjunk)


### Background
[![green-pi](https://img.shields.io/badge/Rendered%20with-Green%20Pi-00d571?style=flat-square)](https://github.com/nschloe/green-pi?activate&inlineMath=$)

The position $x_i$ of the line annotations is computed as the solution of a non-negative
least-squares problem
$$
\begin{align}
\frac{1}{2}\sum_i (x_i - t_i)^2 \to \min_x,\\\\
(x_i - x_j)^2 \ge a^2 \quad \forall i,j.
\end{align}
$$
where $a$ is the minimum distance between two entries and $t_i$ is the target position.


### Testing

To run the dufte unit tests, check out this repository and type
```
pytest
```

### License

This software is published under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
