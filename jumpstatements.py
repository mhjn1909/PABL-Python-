#take 2 inputs from user and multiply them. if result is even,print numbers from 0 to result.execution stops at multiple of 5. if result is odd continue execution even if multiple of 3 is encountered.else pass the execution.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 * num2
if result % 2 == 0:
    for i in range(result):
        if i % 5 == 0 and i != 0:
            break
        print(i)
elif result % 2 != 0:
    for i in range(result):
        if i % 3 == 0 and i != 0:
            continue 
        print(i)
