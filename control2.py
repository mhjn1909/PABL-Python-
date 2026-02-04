#print all the sqares,cubes and prime numbers that are present from zero to n.
n = int(input("Enter the value of n: "))

print("Square numbers:")
for i in range(1, n + 1):
    if i * i <= n:
        print(i * i)

print("\nCube numbers:")
for i in range(1, n + 1):
    if i * i * i <= n:
        print(i * i * i)

print("\nPrime numbers:")
for num in range(2, n + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num)