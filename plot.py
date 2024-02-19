import argparse

import matplotlib.pyplot as plt
import mpld3
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("program")
parser.add_argument("-p", "--port", type=int, default=None)


def main(program):
    data = np.load(f"{program}.npz")

    plt.figure()
    plt.plot(data)
    if port is not None:
        mpld3.show(port=port)
    else:
        plt.show()


if __name__ == "__main__":
    args = parser.parse_args()
    main(**vars(args))
