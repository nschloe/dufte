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


def show(*args, **kwargs):
    plt.show()


# http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
def plot(x, y, label, ygrid=True, fontsize=14):
    p = plt.plot(x, y)

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

    plt.grid(
        axis="y", linestyle="--", dashes=(10, 10), lw=0.5, color="black", alpha=0.3
    )

    # Don't waste space
    plt.autoscale(tight=True)

    # plot "legend" entry
    xlim0, xlim1 = ax.get_xlim()
    plt.text(
        xlim1 + (xlim1 - xlim0) / 100,
        y[-1],
        label,
        fontsize=fontsize,
        verticalalignment="center",
        color=p[0].get_color(),
    )
