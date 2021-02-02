import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy

from .optimize import nnls

# The CIELAB average between GitHub's dark and light font is #71777e. This is hard to
# read on dark background, though, and a little too dark on light background, too. Make
# it lighter. The color #969696 appears to strike a good balance.
_gray = "969696"
_stroke_width = 0.3
# make the xticks slightly wider to make them easier to see
_xtick_width = 0.4

# See <https://matplotlib.org/tutorials/introductory/customizing.html> for all possible
# rcParams.
# TODO move, rotate ylabel <https://github.com/matplotlib/matplotlib/issues/19034>
style = {
    "font.size": 14,
    "text.color": _gray,
    "axes.labelcolor": _gray,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "ytick.minor.left": False,
    # Axes aren't used in this theme, but still set some properties in case the user
    # decides to turn them on.
    "axes.edgecolor": _gray,
    "axes.linewidth": _stroke_width,
    #
    "ytick.right": False,
    "ytick.color": _gray,
    "ytick.major.width": _stroke_width,
    "xtick.minor.top": False,
    "xtick.minor.bottom": False,
    "xtick.color": _gray,
    "xtick.major.width": _xtick_width,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": _gray,
    # Choose the line width such that it's very subtle, but still serves as a guide.
    "grid.linewidth": _stroke_width,
    "axes.xmargin": 0,
    "axes.ymargin": 0,
    # mpl uses category10 by default, dufte uses cat20,
    # <https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#category20>,
    # which basically adds one pale color version of each color in cat10. Change
    # the order such that the first 10 are cat10.
    "axes.prop_cycle": mpl.cycler(
        color=[
            "1f77b4",
            "ff7f0e",
            "2ca02c",
            "d62728",
            "9467bd",
            "8c564b",
            "e377c2",
            "7f7f7f",
            "bcbd22",
            "17becf",
            # pale variants:
            "aec7e8",
            "ffbb78",
            "98df8a",
            "ff9896",
            "c5b0d5",
            "c49c94",
            "f7b6d2",
            "c7c7c7",
            "dbdb8d",
            "9edae5",
        ],
    ),
    "axes.titlepad": 30.0,
    "axes.titlesize": 14,
}


def _move_min_distance(targets, min_distance):
    """Move the targets such that they are close to their original positions, but keep
    min_distance apart.

    https://math.stackexchange.com/a/3705240/36678
    """
    # sort targets
    idx = numpy.argsort(targets)
    targets = numpy.sort(targets)

    n = len(targets)
    x0_min = targets[0] - n * min_distance
    A = numpy.tril(numpy.ones([n, n]))
    b = targets - (x0_min + numpy.arange(n) * min_distance)

    # import scipy.optimize
    # out, _ = scipy.optimize.nnls(A, b)

    out = nnls(A, b)

    sol = numpy.cumsum(out) + x0_min + numpy.arange(n) * min_distance

    # reorder
    idx2 = numpy.argsort(idx)
    sol = sol[idx2]

    return sol


def legend(ax=None, min_label_distance="auto", alpha: float = 1.0):
    ax = ax or plt.gca()

    fig = plt.gcf()

    logy = ax.get_yscale() == "log"

    if min_label_distance == "auto":
        # Make sure that the distance is alpha * fontsize. This needs to be translated
        # into axes units.
        fig_height_inches = fig.get_size_inches()[1]
        ax = plt.gca()
        ax_pos = ax.get_position()
        ax_height = ax_pos.y1 - ax_pos.y0
        ax_height_inches = ax_height * fig_height_inches
        ylim = ax.get_ylim()
        if logy:
            ax_height_ylim = math.log10(ylim[1]) - math.log10(ylim[0])
        else:
            ax_height_ylim = ylim[1] - ylim[0]
        # 1 pt = 1/72 in
        fontsize = mpl.rcParams["font.size"]
        min_label_distance_inches = fontsize / 72 * alpha
        min_label_distance = (
            min_label_distance_inches / ax_height_inches * ax_height_ylim
        )

    # find all Line2D objects with a valid label
    lines = []
    for child in ax.get_children():
        if isinstance(child, mpl.lines.Line2D):
            # https://stackoverflow.com/q/64358117/353337
            if child.get_label()[0] != "_":
                lines.append(child)

    # Add "legend" entries.
    # Get last non-nan y-value.
    targets = []
    for line in lines:
        ydata = line.get_ydata()
        if numpy.all(numpy.isnan(ydata)):
            targets.append(numpy.nan)
        else:
            targets.append(ydata[~numpy.isnan(ydata)][-1])

    if not targets:
        return

    if logy:
        targets = [math.log10(t) for t in targets]

    # Sometimes, the max value if beyond ymax. It'd be cool if in this case we could put
    # the label above the graph (instead of the to the right), but for now let's just
    # cap the target y.
    ymax = ax.get_ylim()[1]
    targets = [min(target, ymax) for target in targets]

    targets = _move_min_distance(targets, min_label_distance)
    if logy:
        targets = [10 ** t for t in targets]

    labels = [line.get_label() for line in lines]
    colors = [line.get_color() for line in lines]

    xlim0, xlim1 = ax.get_xlim()
    for label, t, color in zip(labels, targets, colors):
        plt.text(
            xlim1 + (xlim1 - xlim0) / 100,
            t,
            label,
            verticalalignment="center",
            color=color,
        )
