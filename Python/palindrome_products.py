def largest(min_factor, max_factor):
    product = []
    for a in range(max_factor + 1, min_factor, -1):
        for b in range(max_factor + 1, min_factor, -1):
            mult = a * b
            if str(mult) == str(mult)[::-1]:
                return mult


def smallest(min_factor, max_factor):
    product = []
    for a in range(min_factor, max_factor + 1):
        for b in range(min_factor, max_factor + 1):
            mult = a * b
            if str(mult) == str(mult)[::-1]:
                return mult

print(largest(1000, 9999))
print(smallest(1000, 9999))

print(largest(15, 15))
print(smallest(15, 15))