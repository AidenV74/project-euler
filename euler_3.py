#modules
import time
from math import floor, sqrt

#functions
def find_factors(num):
    limit = floor(sqrt(num))

    #factor out 2 completely
    while num % 2 == 0 and num > 2:
        num = int(num/2)

    #keep factoring out odd numbers until the resulting number is prime
    for i in range(3, limit + 1, 2):

        while num % i == 0 and num / i > 2:
            num = int(num/i)
        
    return num
              

num = int(input("Enter number: \n"))

#start timer
start = time.time()

print("\nLargest Prime Factor of " + str(num) + ": " + str(find_factors(num)))

#end timer
end = time.time()


print(f"runtime: {end-start} seconds")