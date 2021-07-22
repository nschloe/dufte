import matplotlib.pyplot as plt

import dufte


def test_bar():
    with plt.style.context(dufte.style_bar):
        labels = ["label 1", "label 2"]
        vals = [2.1, 6.3]
        xpos = range(len(vals))
        plt.bar(xpos, vals)
        plt.xticks(xpos, labels)
        dufte.show_bar_values("{:.2f}")
        plt.title("some title")


if __name__ == "__main__":
    test_bar()
    plt.show()
    plt.close()
