import math

import matplotlib as mpl
import matplotlib.pyplot as plt

# dufte is used via perfplot on stackoverflow which has a light (#fffff) and a dark
# (#2d2d2d) variant. The midpoint, #969696, should be well readable on both. (And stays
# in the background, like a grid should.)
#
# Twitter background:
#   "Default": #ffffff
#   "Dim": #15202b
#   "Lights out": #000000
_color = "969696"

style = {
    "font.size": 14,
    "text.color": _color,
    "axes.labelcolor": _color,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "ytick.left": False,
    "ytick.right": False,
    "ytick.color": _color,
    "xtick.minor.top": False,
    "xtick.minor.bottom": False,
    "xtick.color": _color,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": _color,
    # Choose the line width such that it's very subtle, but still serves as a guide.
    "grid.linewidth": 0.2,
    "axes.xmargin": 0,
    "axes.ymargin": 0,
    # mpl uses category10 by default, we use cat20,
    # <https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#category20>,
    # which basically adds one pale color version of each color in cat10.  Change
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
}


# https://stackoverflow.com/a/3382369/353337
def _argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


def _move_min_distance(targets, min_distance, eps=1.0e-5):
    """Move the targets such that they are close to their original positions, but keep
    min_distance apart.

    We actually need to solve a convex optimization problem with nonlinear constraints
    here, see <https://math.stackexchange.com/q/3633826/36678>. This algorithm is very
    simplistic.
    """
    idx = _argsort(targets)
    targets = sorted(targets)

    while True:
        # Form groups of targets that must be moved together.
        groups = [[targets[0]]]
        for t in targets[1:]:
            if abs(t - groups[-1][-1]) > min_distance - eps:
                groups.append([])
            groups[-1].append(t)

        if all(len(g) == 1 for g in groups):
            break

        targets = []
        for group in groups:
            # Minimize
            # 1/2 sum_i (x_i + a - target) ** 2
            # over a for a group of labels
            n = len(group)
            pos = [k * min_distance for k in range(n)]
            a = sum(t - p for t, p in zip(group, pos)) / n
            if len(targets) > 0 and targets[-1] > pos[0] + a:
                a = targets[-1] - pos[0] - eps
            new_pos = [p + a for p in pos]
            targets += new_pos

    idx2 = [idx.index(k) for k in range(len(idx))]
    targets = [targets[i] for i in idx2]
    return targets


def legend(ax=None, min_label_distance="auto", alpha=1.4):
    ax = ax or plt.gca()

    fig = plt.gcf()
    # fig.set_size_inches(12 / 9 * height, height)

    logy = ax.get_yscale() == "log"

    if min_label_distance == "auto":
        # Make sure that the distance is alpha times the fontsize. This needs to be
        # translated into axes units.
        fig_height = fig.get_size_inches()[0]
        ax = plt.gca()
        ax_pos = ax.get_position()
        ax_height = ax_pos.y1 - ax_pos.y0
        ax_height_inches = ax_height * fig_height
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

    # find all Line2D objects
    lines = []
    for child in ax.get_children():
        if isinstance(child, mpl.lines.Line2D):
            lines.append(child)

    # Add "legend" entries.
    targets = [line.get_ydata()[-1] for line in lines]
    if logy:
        targets = [math.log10(t) for t in targets]
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
