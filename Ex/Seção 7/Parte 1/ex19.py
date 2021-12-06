val = list()

for a in range(50):
    val.append((a + 5 * a) % (a + 1))

print(val)