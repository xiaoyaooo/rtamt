from rtamt.enumerations.bool_ops import BooleanOperator


def intersection(a, b, method):
    ans = []
    i = j = 1

    hi = None

    while len(a) > 1 and len(b) > 1:
        a_start = a[i - 1][0]
        a_end = a[i][0]
        b_start = b[j - 1][0]
        b_end = b[j][0]

        a_val = a[i - 1][1]
        b_val = b[j - 1][1]


        lo = max(a_start, b_start)
        hi = min(a_end, b_end)

        val = float("nan")
        if lo <= hi:
            val = method(a_val, b_val)
            ans.append((lo, val))

        if a_end < b_end:
            del(a[i-1])
        else:
            del (b[j - 1])

    return ans


def disjunction(a, b):
    return max(a, b)


def conjunction(a, b):
    return min(a, b)


def implication(a, b):
    return max(-a, b)


def xor(a, b):
    return abs(a - b)


def iff(a, b):
    return -abs(a, b)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b
