import numpy

import cleanplotlib as cpl


def test_rand():
    numpy.random.seed(0)

    x0 = numpy.linspace(0.0, 3.0, 100)
    y0 = x0 / (x0 + 1)
    y0 += 0.1 * numpy.random.rand(len(y0))
    cpl.plot(x0, y0, "label")

    x1 = numpy.linspace(0.0, 3.0, 100)
    y1 = 1.5 * x1 / (x1 + 1)
    y1 += 0.1 * numpy.random.rand(len(y1))
    cpl.plot(x1, y1, "long label")

    x2 = numpy.linspace(0.0, 3.0, 100)
    y2 = 1.6 * x2 / (x2 + 1)
    y2 += 0.1 * numpy.random.rand(len(y2))
    cpl.plot(x2, y2, "another label")

    cpl.show()
