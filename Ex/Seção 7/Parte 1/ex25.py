val =list()

for a in range(101):
    if a % 7 != 0 and a % 10 != 7:
        val.append(a)

print(val)