<p align="center">
  <a href="https://github.com/nschloe/dufte"><img alt="dufte-logo" src="https://nschloe.github.io/dufte/logo.svg" width="40%"></a>
  <p align="center"><a href="https://en.wikipedia.org/wiki/Edward_Tufte">Tufte</a>-style plots <a href="https://www.linguee.com/german-english/translation/dufte.html">from Berlin</a>.</p>
</p>

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/dufte/ci?style=flat-square)](https://github.com/nschloe/dufte/actions?query=workflow%3Aci)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/dufte.svg?style=flat-square)](https://pypi.org/pypi/dufte/)
[![PyPi Version](https://img.shields.io/pypi/v/dufte.svg?style=flat-square)](https://pypi.org/project/dufte)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/dufte.svg?logo=github&label=Stars&logoColor=white&style=flat-square)](https://github.com/nschloe/dufte)
[![PyPi downloads](https://img.shields.io/pypi/dm/dufte.svg?style=flat-square)](https://pypistats.org/packages/dufte)

This package creates clean and beautiful plots like

<p align="center">
<img src="https://nschloe.github.io/dufte/ex1.svg" width="70%">
</p>

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
plt.plot(x0, y0, "no balacing")

x1 = numpy.linspace(0.0, 3.0, 100)
y1 = 1.5 * x1 / (x1 + 1)
y1 += 0.1 * numpy.random.rand(len(y1))
plt.plot(x1, y1, "CRV-27")

x2 = numpy.linspace(0.0, 3.0, 100)
y2 = 1.6 * x2 / (x2 + 1)
y2 += 0.1 * numpy.random.rand(len(y2))
plt.plot(x2, y2, "CRV-27*")

dufte.legend()

plt.show()
```
Further reading:

 * [Randal S. Olson's blog entry](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
 * [prettyplotlib](https://github.com/olgabot/prettyplotlib)
 * [Wikipedia: Chartjunk](https://en.wikipedia.org/wiki/Chartjunk)


### Testing

To run the dufte unit tests, check out this repository and type
```
pytest
```

### License

This software is published under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
