import numba as nb


@nb.njit
def fastPow(a: nb.types.longlong, b: nb.types.longlong) -> nb.types.longlong:
    acc = 1
    res = a

    while b > 0:

        if b & 1:
            acc *= res
        res *= res
        b >>= 1

    return acc


for i in range(1, 13):
    print(fastPow(2, 10 * i))
