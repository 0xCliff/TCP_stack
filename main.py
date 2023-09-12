from Layer_1 import NetworkGraph
from topologies import *


def main():
    star = build_star_topology()
    print(star.__repr__())


if __name__ == "__main__":
    main()
