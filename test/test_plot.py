import matplotlib.pyplot as plt
import numpy
import pytest

import dufte


@pytest.mark.parametrize(
    "filename, light, noise, offsets",
    [[None, True, 0.1, (1.0, 1.50, 1.60)], [None, True, 0.0, (1.0, 1.50, 1.51)]],
)
def test_plot(filename, light, noise, offsets):
    plt.style.use(dufte.style)

    numpy.random.seed(0)
    x0 = numpy.linspace(0.0, 3.0, 100)
    labels = ["no balancing", "CRV-27", "CRV-27*"]
    for label, offset in zip(labels, offsets):
        y0 = offset * x0 / (x0 + 1)
        y0 += noise * numpy.random.rand(len(y0))
        plt.plot(x0, y0, label=label)

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
    test_plot("ex1-light.svg", True, 0.1, (1.0, 1.5, 1.6))
    # test_plot("ex1-dark.svg", light=False)
