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
    if (0 <= i < len(str1)) & (0 <= j < len(str2)):
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

n = 100
a = [1,1,0,0,0,0,1,1]
b = [0,0,1,1,1,1,0,0]
probability = prob(a,b,n)

x = np.array([(x / n) for x in range(1, n)])
y = np.array(probability)
ymax = max(y)
ymin = min(y)
x2 = []
y2 = []

plt.figure(figsize=(10,7))
plt.plot(x, y, linestyle = 'solid', zorder = 1)
for xitem, yitem in np.nditer([x,y]):
    if yitem == ymax or yitem == ymin:
        x2.append(xitem)
        y2.append(yitem)
plt.scatter(x2, y2, color = "red", zorder = 2)
astr = "".join(str(x) for x in a)
bstr = "".join(str(x) for x in b)
title1 = "Probability " + bstr + " appears before " + astr
title2 = "Probability of generating 0"
plt.title(bstr + " vs "  + astr, fontsize = 20, pad = 10)
plt.xlabel(title2, fontsize = 14, labelpad = 15)
plt.ylabel(title1, fontsize = 14, labelpad = 20)
plt.show()
