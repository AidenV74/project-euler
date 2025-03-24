import time

def sum_of_squares(lower_limit, upper_limit):
    sum = 0
    for i in range(lower_limit, upper_limit + 1):
        sum += i*i
    return sum
    
def square_of_sum(lower_limit, upper_limit):
    sum = 0
    for i in range(lower_limit, upper_limit + 1):
        sum += i
    return sum*sum

low = 1
high = 100

start = time.time()

print("sum of squares: " + str(sum_of_squares(low, high)))
print("square of sum: " + str(square_of_sum(low, high)))

print("The difference between the square of the sum and the sum of the squares is " + str(square_of_sum(low, high) - sum_of_squares(low, high)))

end = time.time()

print(f"runtime: {end-start} seconds")