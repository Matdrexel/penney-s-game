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
                    if not contains(a, b):
                        odds = odds_b_before_a(a, b)
                        if odds[0] > odds[1]:
                            print(odds, a, b)
                            curr = [odds, a, b]
                            entry = ', '.join(str(x) for x in curr)
                            results.append(entry)
                j += 1
        print(i)
        i += 1
    with open('long_short_string.txt', 'w') as f:
        f.writelines('\n'.join(results))
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
    # copied from LongShortString.py
    if i == 0:
        return 1 / p
    elif i == 1:
        return 1 / (1 - p)


search(1, 6)

# %%
