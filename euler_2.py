#runs through all of the fibonacci numbers below 4 million and appends them to the evenFib list if it is even.
def evenFibonacci():
    evenFib = [2]
    num1 = 1
    num2 = 2
    num3 = 0
    while num1 + num2 <= 4000000: 
        num3 = num1 + num2
        if num3 % 2 == 0:
            evenFib.append(num3)
        num1 = num2
        num2 = num3
    return evenFib

print(evenFibonacci())
print("Sum: " + str(sum(evenFibonacci())))