##################################################
###### IF YOU WORK BY GROUP OF TWO ###############
###### ENTER YOUR TWO NAMES HERE:  ###############
###### Name1 = Anush Bhavesh Rathod (Student id - 32914218)
###### Name2= Maheer Daiyan (Student Id - 32594014)
######
###### Only 1 submission on moodle (either names ok)
##################################################

import numpy as np
import matplotlib.pyplot as plt

def main():
    """Taking approximations of pi from a sample size"""

    # initializing all the variable required
    np.random.seed(5)
    n = 1000000
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    d = x**2 + y**2
    pi = np.empty(n)
    m = 0

    power = 1  # temp variable used for printing
    temp = 1  # also used during printing

    for i in range(n):  # sets the value of pi in each index of the array as per the formula
        if np.sqrt(d[i]) <= 1:
            m = m + 1
            pi[i] = (4/float(i+1)) * m
        else:
            pi[i] = (4/float(i+1)) * m

    # printing the value of pi for each sample size
    while True:
        print("Using %s samples, pi is %g" % (10**power, pi[(10**power)-1]))
        temp += 1
        power += 1
        if temp == 7:
            break


    # plotting the first graph of pi
    plt.figure(0)
    plt.semilogx(pi)
    plt.ylim(1.5, 4)
    plt.xlabel("#samples")
    plt.ylabel("pi")

    # plotting all the circular plots
    plt.figure(1)

    theta = np.arange(360) * 2 * np.pi / 360  # for plotting the circles
    xi = np.cos(theta)
    yi = np.sin(theta)

    # first circle plot with pi values till sample 10
    plt.subplot(2, 2, 1)
    plt.plot(xi, yi)  # plotting the circle
    plt.axis('equal')
    plt.scatter([x[i] for i in range(10)], [y[i] for i in range(10)], c="r")  # plotting the scatter marks
    plt.title("n=10" + ", pi= %.3f " % (pi[9]))  # printing the title
    plt.xticks([])
    plt.yticks([])

    # second circle plot with pi values till sample 100
    plt.subplot(2, 2, 2)
    plt.scatter([x[i] for i in range(100)], [y[i] for i in range(100)], c="r")
    plt.plot(xi, yi)
    plt.axis('equal')
    plt.title("n=100" + ", pi= %.3f " % (pi[99]))
    plt.xticks([])
    plt.yticks([])

    # third circle plot with pi values till sample 1000
    plt.subplot(2, 2, 3)
    plt.scatter([x[i] for i in range(1000)], [y[i] for i in range(1000)], c="r")
    plt.plot(xi, yi)
    plt.axis('equal')
    plt.title("n=1000" + ", pi= %.3f " % (pi[999]))
    plt.xticks([])
    plt.yticks([])

    # fourth circle plot with pi values till sample 10000
    plt.subplot(2, 2, 4)
    plt.scatter([x[i] for i in range(10000)], [y[i] for i in range(10000)], c="r")
    plt.plot(xi, yi)
    plt.axis('equal')
    plt.title("n=10000" + ", pi= %.3f " % (pi[9999]))
    plt.xticks([])
    plt.yticks([])


    plt.show()

if __name__ == "__main__":
    main()











