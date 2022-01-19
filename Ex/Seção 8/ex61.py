def anagrama(a, b):
    if len(a) != len(b):
        return False
    for c in range(len(a)):
        if a[c] not in b or b[c] not in a:
            return False
    return True

print(anagrama('banana', 'anabad'))