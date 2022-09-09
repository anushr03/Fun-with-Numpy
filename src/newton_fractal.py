import numpy as np
import matplotlib.pyplot as plt

def main():
    """function to calculate newton fractal"""

    # taking user input
    n = input("Newton fractal z**n=1, Enter n (default 3): ")
    if n == "":
        n = 3
    n = int(n)

    cords = input("Enter xmin,xmax,ymin,ymax (default -1.35,1.35,-1.35,1.35): ")
    if cords == "":
        xmin = -1.35
        xmax = 1.35
        ymin = -1.35
        ymax = 1.35
    else:
        xmin, xmax, ymin, ymax = cords.split()
        xmin = float(xmin)
        xmax = float(xmax)
        ymin = float(ymin)
        ymax = float(ymax)
    print("Solutions are")

    sol = [0] * n

    for m in range(n): # printing the solutions
        sol[m] = np.exp(1j * ((2 * np.pi * m) / n))
        print(sol[m])

    x = np.linspace(xmin+0.00011, xmax, 1000)  # initializing x and y array
    y = np.linspace(ymin+0.00011, ymax, 1000)

    C = np.zeros((1000, 1000), dtype=complex)

    for i in range(1000):  # calculating and storing values in Matrix C
        for j in range(1000):
            C[i, j] = x[j] + 1j * y[i]

    for i in range(20):  # making 20 Newton iteration on each value in Matrix C
        C = C - (C / n) + (1 / n) * (1 / C)**(n-1)


    color_array = np.zeros((1000, 1000), dtype=int)

    for i in range(1000):  # getting the C shape array for the root solutions
        for j in range(1000):
            index = -1
            low = float('inf')  # initializing arbitrary value to find the smallest error in the array
            element = C[i, j]
            for m in range(len(sol)):
                error = abs(element-sol[m])/abs(sol[m])
                if error < low:  # looking for the value with the smallest error
                    low = error
                    index = m
            color_array[i, j] = (index * 255) / (n - 1)




    # Plotting the function's root
    plt.imshow(color_array, cmap="rainbow", interpolation="bilinear", origin="lower", extent=[xmin, xmax, ymin, ymax])
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()

if __name__ == "__main__":
    main ()
