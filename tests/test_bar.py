import matplotlib.pyplot as plt

import dufte


def test_bar(filename=None, light=True):
    with plt.style.context(dufte.style_bar):
        labels = ["Australia", "Brazil", "China", "Germany", "Mexico", "United\nStates"]
        vals = [21.65, 24.5, 6.95, 8.40, 21.00, 8.55]
        xpos = range(len(vals))
        plt.bar(xpos, vals)
        plt.xticks(xpos, labels)
        dufte.show_bar_values("{:.2f}")
        plt.title("average temperature [°C]")

        if not light:
            gh_dark_bg = "#0d1117"
            plt.gca().set_facecolor(gh_dark_bg)
            plt.gcf().patch.set_facecolor(gh_dark_bg)

    if filename:
        plt.savefig(filename, transparent=True, bbox_inches="tight")
    else:
        plt.show()


if __name__ == "__main__":
    # test_bar("bar-light.svg", True)
    # plt.close()
    # test_bar("bar-dark.svg", False)
    test_bar("bar.svg", False)
    plt.close()
