# cleanplotlib

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/cleanplotlib/ci?style=flat-square)](https://github.com/nschloe/cleanplotlib/actions?query=workflow%3Aci)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/cleanplotlib.svg?style=flat-square)](https://pypi.org/pypi/cleanplotlib/)
[![PyPi Version](https://img.shields.io/pypi/v/cleanplotlib.svg?style=flat-square)](https://pypi.org/project/cleanplotlib)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/cleanplotlib.svg?logo=github&label=Stars&logoColor=white&style=flat-square)](https://github.com/nschloe/cleanplotlib)
[![PyPi downloads](https://img.shields.io/pypi/dm/cleanplotlib.svg?style=flat-square)](https://pypistats.org/packages/cleanplotlib)

This package creates clean, beautiful matplotlib plots like

<p align="center">
<img alt="dmsh" src="https://nschloe.github.io/cleanplotlib/ex1.svg" width="70%">
</p>

The plot is created with
```python
import cleanplotlib as cpl
import numpy

numpy.random.seed(0)

x0 = numpy.linspace(0.0, 3.0, 100)
y0 = x0 / (x0 + 1)
y0 += 0.1 * numpy.random.rand(len(y0))
cpl.plot(x0, y0, "no balacing")

x1 = numpy.linspace(0.0, 3.0, 100)
y1 = 1.5 * x1 / (x1 + 1)
y1 += 0.1 * numpy.random.rand(len(y1))
cpl.plot(x1, y1, "CRV-27")

x2 = numpy.linspace(0.0, 3.0, 100)
y2 = 1.6 * x2 / (x2 + 1)
y2 += 0.1 * numpy.random.rand(len(y2))
cpl.plot(x2, y2, "CRV27*")

cpl.show()
# cpl.savefig("ex1.svg", transparent=True, bbox_inches="tight")
```

Further reading:

 * [Randal S. Olson's blog entry](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
 * [prettyplotlib](https://github.com/olgabot/prettyplotlib)


### Testing

To run the cleanplotlib unit tests, check out this repository and type
```
pytest
```

### License

This software is published under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
