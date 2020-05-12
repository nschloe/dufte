import matplotlib.pyplot as plt
import numpy

import dufte


def test_plot(filename=None, light=True):
    plt.style.use(dufte.style)

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
    dufte.legend()

    if not light:
        plt.gca().set_facecolor("#2d2d2d")
        plt.gcf().patch.set_facecolor("#2d2d2d")

    if filename:
        # <https://github.com/matplotlib/matplotlib/issues/17321>
        plt.savefig(
            filename,
            transparent=True,
            bbox_inches="tight",
            facecolor=plt.gcf().get_facecolor(),
        )
    else:
        plt.show()


if __name__ == "__main__":
    test_plot("ex1-light.svg")
    # test_plot("ex1-dark.svg", light=False)
