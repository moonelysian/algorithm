numbers = set(range(1,10001))
generated = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated.add(i)

selfNumbers = numbers - generated

for i in sorted(selfNumbers):
    print(i)