import matplotlib as mpl
import matplotlib.pyplot as plt

# mpl uses category10 by default, we use cat20,
# <https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#category20>,
# which basically adds one pale color version of each color in cat10.
# Change the order such that the first 10 are cat10.
mpl.rcParams["axes.prop_cycle"] = mpl.cycler(
    color=[
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
        # pale variants:
        "#aec7e8",
        "#ffbb78",
        "#98df8a",
        "#ff9896",
        "#c5b0d5",
        "#c49c94",
        "#f7b6d2",
        "#c7c7c7",
        "#dbdb8d",
        "#9edae5",
    ]
)


# https://stackoverflow.com/a/3382369/353337
def _argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


def show(*args, **kwargs):
    plt.show()


# http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
def plot(x, y, label, ygrid=True, fontsize=14, height=5):
    multiplot([x], [y], [label], ygrid=ygrid, fontsize=fontsize, height=height)


def _move_min_distance(targets, min_distance, eps=1.0e-5):
    """Move the targets such that they are close to their original positions, but keep
    min_distance apart.

    We actually need to solve a convex optimization problem with nonlinear constraints
    here, see <https://math.stackexchange.com/q/3633826/36678>. This algorithm is very
    simplistic.
    """
    assert targets == sorted(targets)
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
    return targets


def multiplot(x, y, labels, min_label_distance=0.0, ygrid=True, fontsize=14, height=5):
    p = [plt.plot(xx, yy) for xx, yy in zip(x, y)]

    fig = plt.gcf()
    fig.set_size_inches(16 / 9 * height, height)

    # > Remove the plot frame lines. They are unnecessary chartjunk.
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.tick_params(length=0)

    # > Make sure your axis ticks are large enough to be easily read.
    # > You don't want your viewers squinting to read your plot.
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)

    if ygrid:
        plt.grid(axis="y", dashes=(10, 10), lw=0.5, color="black", alpha=0.3)

    # Don't waste space
    plt.autoscale(tight=True)

    # Add "legend" entries.
    targets = [yy[-1] for yy in y]
    idx = _argsort(targets)
    targets = _move_min_distance(sorted(targets), min_label_distance)
    targets = [targets[i] for i in idx]

    xlim0, xlim1 = ax.get_xlim()
    for yy, label, t, pp in zip(y, labels, targets, p):
        plt.text(
            xlim1 + (xlim1 - xlim0) / 100,
            t,
            label,
            fontsize=fontsize,
            verticalalignment="center",
            color=pp[0].get_color(),
        )
