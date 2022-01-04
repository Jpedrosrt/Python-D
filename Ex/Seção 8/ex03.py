def pos_or_neg_or_0(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

print(pos_or_neg_or_0(0))