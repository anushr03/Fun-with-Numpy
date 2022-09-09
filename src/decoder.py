import numpy as np
import matplotlib.pyplot as plt
def main():
    # taking input from the user
    name = input("Enter compressed coordinate matrix file name: ")

    # load entire matrix
    x, y, colour_value = np.loadtxt(name, unpack=True, dtype=float).astype(int)

    image = np.zeros((max(x) + 1, max(y) + 1))

    for i in range(len(x)):  # making a 2D array of the image
        image[x[i], y[i]] = colour_value[i]

    plt.imshow(image, cmap="binary")
    plt.show()


if __name__ == "__main__":
    main()