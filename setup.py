import os
from setuptools import setup

if __name__ == "__main__":
    # TODO move this into setup.cfg somehow
    # <https://stackoverflow.com/q/61525076/353337>
    setup(
        data_files=[
            (
                "{}/.config/matplotlib/stylelib/".format(os.environ["HOME"]),
                ["dufte/dufte.mplstyle"],
            )
        ],
    )
