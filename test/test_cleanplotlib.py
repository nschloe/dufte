from pathlib import Path
import numpy

import matplotlib.pyplot as plt
import cleanplotlib as cpl


def test_plot(filename=None):
    this_dir = Path(__file__).resolve().parent
    style_file = str(this_dir.parent / "cleanplotlib/cleanplotlib.mplstyle")
    print(style_file)
    plt.style.use(style_file)

    numpy.random.seed(0)
    x0 = numpy.linspace(0.0, 3.0, 100)
    y0 = x0 / (x0 + 1)
    y0 += 0.1 * numpy.random.rand(len(y0))
    plt.plot(x0, y0, label="no balancing")

    x1 = numpy.linspace(0.0, 3.0, 100)
    y1 = 1.5 * x1 / (x1 + 1)
    y1 += 0.1 * numpy.random.rand(len(y1))
    plt.plot(x1, y1, label="CRV-27")

    x2 = numpy.linspace(0.0, 3.0, 100)
    y2 = 1.6 * x2 / (x2 + 1)
    y2 += 0.1 * numpy.random.rand(len(y2))
    plt.plot(x2, y2, label="CRV-27*")

    # plt.xlabel("x label")
    # plt.ylabel("y label")
    # plt.title("title")
    cpl.legend()

    if filename:
        plt.savefig(filename, transparent=True, bbox_inches="tight")
    else:
        plt.show()


# def test_multiplot():
#     plt.style.use(str(this_dir.parent / "cleanplotlib/cleanplotlib.mplstyle"))
#     numpy.random.seed(0)
#
#     x = numpy.linspace(0.0, 3.0, 100)
#     y0 = x / (x + 1)
#     # y0 += 0.1 * numpy.random.rand(len(y0))
#     y1 = 1.01 * x / (x + 1)
#     # y1 += 0.1 * numpy.random.rand(len(y1))
#     y2 = 1.03 * x / (x + 1)
#     # y2 += 0.1 * numpy.random.rand(len(y2))
#
#     cpl.multiplot(
#         [x, x, x], [y0, y1, y2], ["label", "long label", "another long label"]
#     )
#
#     cpl.show()


if __name__ == "__main__":
    plt.rc("font", family="Helvetica World")
    # test_plot("ex1.svg")
    test_plot()
