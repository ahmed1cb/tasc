"""

Tasc V0.1.0

The best way to manage Tasks from Your Terminal Easly

"""

# Pythons Mods
import sys

# App Components
from . import Tasc


def main():
    app = Tasc()
    app.handle(sys.argv[1:])
