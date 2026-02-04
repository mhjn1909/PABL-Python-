#take choice from user,if choice is 1 then calculate fibonacci series upto n,
#if choice is 2 then calculate tribonacci upto n.
n = int(input("Enter the value of n: "))
choice = int(input("Enter 1 for Fibonacci series and 2 for Tribonacci series: "))
if choice == 1:
    print("Fibonacci series up to", n, ":")
    a, b = 0, 1
    while a <= n:
        print(a)
        a, b = b, a + b
elif choice == 2:
    print("Tribonacci series up to", n, ":")
    a, b, c = 0, 0, 1
    while a <= n:
        print(a)
        a, b, c = b, c, a + b + c