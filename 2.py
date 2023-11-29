def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

numb = [5, 7, 10, 3, 8]

results = []

for num in numb:
    fac = fact(num)
    results.append(str(fac))

print(", ".join(results))