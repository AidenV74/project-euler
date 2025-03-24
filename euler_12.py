def factors(n):    
   factors = []
   step = 2 if n % 2 else 1
   for i in range(1, int(n ** 0.5) + 1, step):
       if n % i == 0:
           factors.append(i)
           if n / i not in factors:
               factors.append(int(n / i))
   factors.sort()
   return factors
 
def triangle_numbers(range):
    triangle_numbers = []
    triangle_factors = []
    
    num = 2
    sum = 1
    while sum <= range:
        triangle_numbers.append(sum)
        if len(factors(sum)) > 500:
            return sum
        sum += num
        num += 1

print(triangle_numbers(100000000))