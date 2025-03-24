def sum_digits(num):
    
    digits = []
    
    num = str(num)
    for digit in num:
        digits.append(int(digit))
    print("Sum of the digits in the number " + str(num) + ": " + str(sum(digits)))
    
sum_digits(2 ** 1000)