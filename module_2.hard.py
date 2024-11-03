import random
a = random.randint (3, 20)
print(a)
result = []

for i in range(1, a+1):
    for k in range(1,20):
        if a % (k+i) == 0 and i != 0 and i < k:
            result.append(i)
            result.append(k)
print("".join(map(str, result)))





