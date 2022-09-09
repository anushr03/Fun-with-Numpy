import math

def main():
    """Finding square out of number using N-R iteration method"""

    N = input("Square root of which number? ")  # the int whose sqrt has to be calculated
    N = float(N)
    x_i = 1  # Initial guess for x0
    count = 1
    result = math.sqrt(N)
    while True:
        x_i1 = x_i - (((x_i**2) - N) / (2 * x_i))  # formula for finding the next number
        print("%s %s" % (count, x_i1))

        if abs(x_i1 - result) / abs(result) < 1e-15:  # Stopping the loop if the root is within the tolerance
            break
        else:
            x_i = x_i1
            count += 1

if __name__ == "__main__":
    main()
