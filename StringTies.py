results = []


def search(start, end):
    i = start
    while i <= end:
        for m in range(2 ** i):
            b = zeroed_bin_list(m, i)
            for n in range(m + 1, 2 ** i):
                a = zeroed_bin_list(n, i)
                odds = odds_b_before_a(a, b)
                if (odds[0] == odds[1]) & (odds[0] != 0):
                    curr = [a, b]
                    s = ''.join(str(x) for x in curr)
                    results.append(s)
                    print(a, b)
        i += 1
    # with open('4-5_ties.txt', 'w') as f:
    #     f.writelines('\n'.join(results))
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
        for j in range(i, m - i):
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


search(4, 5)

# %%
