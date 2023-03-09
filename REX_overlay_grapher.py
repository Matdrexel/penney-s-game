import numpy as np
import matplotlib.pyplot as plt
import scipy
from numpy.polynomial.polynomial import Polynomial

def odds_b_before_a(a, b, p):
    top = star(a, a, p) - star(a, b, p)
    bot = star(a, a, p) + star(b, b, p) - star(a, b, p) - star(b, a, p)
    return top / bot


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
    if (0 <= i < len(str1)) and (0 <= j < len(str2)):
        if str1[i] == str2[j]:
            return inverse_p(str2[j], p)
        else:
            return 0
    else:
        return 0


def inverse_p(i, p):
    if i == 0:
        return (1 / p)
    elif i == 1:
        return (1 / (1 - p))

def prob(a, b, n):
    res = []
    for i in range(1, n):
        p = i / n
        res.append(odds_b_before_a(a, b, p))
    return res

def coin(x):
    if x == 0:
        return "H"
    elif x == 1:
        return "T"

n = 100
a = [0,1,1,1,1,1,0,1]
b = [1,1,0,1,0,1,1,1]
a2 = [1,1,0,0,0,0,1,1]
b2 = [0,0,1,1,1,1,0,0]
a3 = [0,0,0,0,1,1,1,0]
b3 = [0,0,0,1,0,0,1,1]
a4 = [0,1,1,0,1,0,0,1]
b4 = [1,0,0,1,0,1,1,0]
probability = prob(a,b,n)
probability2 = prob(a2,b2,n)
probability3 = prob(a3,b3,n)
probability4 = prob(a4,b4,n)

x = np.array([(x / n) for x in range(1, n)])
y = np.array(probability)
y2 = np.array(probability2)
y3 = np.array(probability3)
y4 = np.array(probability4)


plt.figure(figsize=(10,7))

plt.plot(x, y, linestyle = 'solid', color = "blue", label = "".join(coin(x) for x in b) + " vs " + "".join(coin(x) for x in a))

plt.plot(x, y2, linestyle = 'solid', color = "green", label = "".join(coin(x) for x in b2) + " vs " + "".join(coin(x) for x in a2))

plt.plot(x, y3, linestyle = 'solid', color = "red", label = "".join(coin(x) for x in b3) + " vs " + "".join(coin(x) for x in a3))

plt.plot(x, y4, linestyle = 'solid', color = "orange", label = "".join(coin(x) for x in b4) + " vs " + "".join(coin(x) for x in a4))

title1 = "Probability the first sequence appears before the second"
title2 = "Probability of a coin landing on Heads"
plt.title("Sequences of length 8", fontsize = 20, pad = 10)
plt.xlabel(title2, fontsize = 14, labelpad = 15)
plt.ylabel(title1, fontsize = 14, labelpad = 20)
plt.legend()
plt.show()