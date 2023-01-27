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
                    odds = odds_b_before_a(a, b)
                    if odds[0] >= odds[1]:
                        results.append([odds[0], odds[1], a, b])
                        print(a, b)
                j += 1
        print(i)
        i += 1
    print(results)
    print("done")


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


def odds_b_before_a(a, b):
    return [star(a, a) - star(a, b), star(b, b) - star(b, a)]


def star(str1, str2):
    result = 0
    m = len(str1)
    for i in range(m):
        product = 1
        for j in range(i, m):
            product *= delta(j, j - i, str1, str2)
        result += product
    return result


def delta(i, j, str1, str2):
    if (0 <= i < len(str1)) & (0 <= j < len(str2)):
        if str1[i] == str2[j]:
            return inverse_p(str2[j])
        else:
            return 0
    else:
        return 0


def inverse_p(i):
    return 2


search(1, 11)

# %%
