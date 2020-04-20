import numpy

import cleanplotlib as cpl


def test_plot():
    numpy.random.seed(0)

    x0 = numpy.linspace(0.0, 3.0, 100)
    y0 = x0 / (x0 + 1)
    y0 += 0.1 * numpy.random.rand(len(y0))
    cpl.plot(x0, y0, "no balancing")

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


def test_multiplot():
    numpy.random.seed(0)

    x = numpy.linspace(0.0, 3.0, 100)
    y0 = x / (x + 1)
    # y0 += 0.1 * numpy.random.rand(len(y0))
    y1 = 1.01 * x / (x + 1)
    # y1 += 0.1 * numpy.random.rand(len(y1))
    y2 = 1.03 * x / (x + 1)
    # y2 += 0.1 * numpy.random.rand(len(y2))

    cpl.multiplot(
        [x, x, x], [y0, y1, y2], ["label", "long label", "another long label"]
    )

    cpl.show()
