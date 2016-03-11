items = [1, 2, 3, 4, 5]

# NO MAPPING

square = []
for item in items:
    square.append(item ** 2)

print square


def sqrEvens(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return 0


result = map(sqrEvens, items)

print result

evens = filter(lambda a:a!=0, result)
print evens