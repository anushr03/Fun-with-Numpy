import numpy as np
import matplotlib.pyplot as plt

def main():
    """Taking approximations of the area of a triangle of different sample size"""
    np.random.seed(7)
    n = 100000

    # User Input point 1
    point1 = input("Enter (x,y) of  point-1, default is (0.5,0.5): ")
    if point1 == "":
        x1 = 0.5
        y1 = 0.5
    else:
        x1, y1 = point1.split()
        x1 = float(x1)
        y1 = float(y1)

    # User input point 2
    point2 = input("Enter (x,y) of  point-2, default is (3,2.5): ")
    if point2 == "":
        x2 = 3
        y2 = 2.5
    else:
        x2, y2 = point2.split()
        x2 = float(x2)
        y2 = float(y2)

    # user input point 3
    point3 = input("Enter (x,y) of  point-3, default is (1,3): ")
    if point3 == "":
        x3 = 1
        y3 = 3
    else:
        x3, y3 = point3.split()
        x3 = float(x3)
        y3 = float(y3)

    arr = np.array([[x1, x2, x3], [y1, y2, y3], [1, 1, 1]])
    print("Barycentric Matrix\n", arr)

    xmin = min(x1, x2, x3)
    xmax = max(x1, x2, x3)
    ymin = min(y1, y2, y3)
    ymax = max(y1, y2, y3)

    # calculating the domain and initializing the random x y values
    x = np.random.uniform(xmin, xmax, n)
    y = np.random.uniform(ymin, ymax, n)
    d = (ymax-ymin) * (xmax-xmin)

    area = np.empty(n)  # initializing the area array. area is area of the triangle
    m = 0

    for i in range(n):
        variable_array = np.array([[x[i]], [y[i]], [1]])  # initializing the random x and y matrix
        coeff = np.linalg.solve(arr, variable_array)  # solving for the coeff by linear alebgra
        a1 = coeff[0]
        a2 = coeff[1]
        a3 = coeff[2]

        if a1 > 0 and a2 > 0 and a3 > 0:
            m += 1
            area[i] = (d/float(i+1)) * m
        else:
            area[i] = (d/float(i+1)) * m

    # printing the value of area for each sample size
    temp = 1
    power = 1
    while True:
        print("Using %s samples, area of triangle is %g" % (10 ** power, area[(10 ** power) - 1]))
        temp += 1
        power += 1
        if temp == 6:
            break

    # plotting the graph
    plt.figure(0)
    plt.semilogx(area)
    plt.xlabel("#samples")
    plt.ylabel("Area-Triangle")

    # initializing all the triangle plots coordinates
    plt.figure(1)
    xt = [x1, x2, x3, x1]
    yt = [y1, y2, y3, y1]

    # first triangle plot with area values till sample 10
    plt.subplot(2, 2, 1)
    plt.scatter([x[i] for i in range(10)], [y[i] for i in range(10)], c="r")  # plotting the scatter marks
    plt.plot(xt, yt)  # plotting the triangle
    plt.title("n=10" + ", area= %.3f " % (area[9]))  # printing the title
    plt.xticks([])
    plt.yticks([])

    # second triangle plot with area values till sample 100
    plt.subplot(2, 2, 2)
    plt.scatter([x[i] for i in range(100)], [y[i] for i in range(100)], c="r")
    plt.plot(xt, yt)
    plt.title("n=100" + ", area= %.3f " % (area[99]))
    plt.xticks([])
    plt.yticks([])

    # third triangle plot with area values till sample 1000
    plt.subplot(2, 2, 3)
    plt.scatter([x[i] for i in range(1000)], [y[i] for i in range(1000)], c="r")
    plt.plot(xt, yt)
    plt.title("n=1000" + ", area= %.3f " % (area[999]))
    plt.xticks([])
    plt.yticks([])

    # fourth triangle plot with area values till sample 10000
    plt.subplot(2, 2, 4)
    plt.scatter([x[i] for i in range(10000)], [y[i] for i in range(10000)], c="r")
    plt.plot(xt, yt)
    plt.title("n=10000" + ", area= %.3f " % (area[9999]))
    plt.xticks([])
    plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main ()
