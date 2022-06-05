row = [3, 4, 56, 100, 15, 2, 20, 30]
result = 1
for i in row:
    if i % 3 == 0 and i % 5 == 0:
        result *= i
print(result)