#loops through the numbers in a given range and returns the largest palindrome found
def find_palindrome(maximum, minimum):
    palindrome_list = []
    for i in range(maximum, minimum - 1, -1):
        for j in range(maximum, minimum - 1, -1):
            product = i * j
            reverse_product = reverse_number(product)
            if product == reverse_product:
                palindrome_list.append(product)
    max_palindrome = max(palindrome_list)
    return max_palindrome

#a function for reversing a number           
def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r

#loops through all 3 digit numbers
print(find_palindrome(999, 100))