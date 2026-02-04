#Take input from user and find all the prime factors of that number.
n = int(input("Enter a number to find its prime factors: "))
print("Prime factors of", n, "are:")
for i in range(2, n + 1):
    while n % i == 0:
        print(i)
        n = n // i
        