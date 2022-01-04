def perfect_square(n):
    if int(n ** 0.5) ** 2 == n:
        return 'perfect square'
    return "it's not a perfect square"

print(perfect_square(4))
