import numpy as np
import matplotlib.pyplot as plt

results = []


def search(start, end):
    i = start
    while i <= end:
        for m in range(2 ** i):
            b = zeroed_bin_list(m, i)
            j = 1
            while j < i:
                for n in range(2 ** j):
                    a = zeroed_bin_list(n, j)
                    if not contains(a, b):  # implement selector functions here
                        x = np.linspace(0.0001, 1, 100)
                        y = odds_b_before_a(a, b, x)
                        plt.plot(x, y)
                j += 1
        print(i)
        i += 1
    # Naming the x-axis, y-axis and the whole graph
    plt.xlabel("p (probability of 0)")
    plt.ylabel("odds of b")
    plt.title("Odds of B winning")
    # Adding legend, which helps us recognize the curve according to it's color
    # plt.legend()

    # To load the display window
    plt.show()
    print("done")


# stolen from stack overflow:
# https://stackoverflow.com/questions/20789412/check-if-all-elements-of-one-array-is-in-another-array
def contains(short, long):
    len_s = len(short)
    return any(short == long[i:len_s + i] for i in range(len(long) - len_s + 1))


def zeroed_bin_list(i, size):
    result = []
    r = bin_list(i)
    for j in range(size - len(r)):
        result.append(0)
    result.extend(r)
    return result


def bin_list(x):
    if x == 0:
        return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]


def odds_b_before_a(a, b, p):
    return (star(a, a, p) - star(a, b, p))/(star(b, b, p) - star(b, a, p) + star(a, a, p) - star(a, b, p))


def star(str1, str2, p):
    result = 0
    m = len(str1)
    for i in range(m):
        product = 1
        for j in range(i, m):
            product *= delta(j, j - i, str1, str2, p)
        result += product
    return result


def delta(i, j, str1, str2, p):
    if (0 <= i < len(str1)) & (0 <= j < len(str2)):
        if str1[i] == str2[j]:
            return inverse_p(str2[j], p)
        else:
            return 0
    else:
        return 0


def inverse_p(i, p):
    # copied from LongShortString.py
    if i == 0:
        return 1 / p
    elif i == 1:
        return 1 / (1 - p)


search(6, 6)

p = np.linspace(0.0001, 1, 100)
# q = odds_b_before_a([0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0], p) -> weird!
# q = odds_b_before_a([0, 1, 1, 0], [1, 0, 1, 0], p) -> straight line
# q = odds_b_before_a([1, 1, 0, 1], [0, 1, 1, 1], p) -> weird
plt.plot(p, q)

plt.show()
