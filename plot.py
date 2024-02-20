import argparse

import matplotlib.pyplot as plt
import mpld3
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("program")
parser.add_argument("-p", "--port", type=int, default=None)


def main(program, port):
    data = np.load(f"data/{program}.npz")

    plt.figure()
    plt.suptitle(program)
    for key, value in data.items():
        if "-" not in key:
            plt.plot(value, label=key)
    plt.legend()

    if port is not None:
        mpld3.show(port=port)
    else:
        plt.show()


if __name__ == "__main__":
    args = parser.parse_args()
    main(**vars(args))
