import time

def find_lcm(lower_limit, upper_limit):
    found_lcm = 1
    num = upper_limit
    while found_lcm == 1:
        for i in range(lower_limit, upper_limit):
            if num / i % 1 != 0:
                found_lcm = 0
        if found_lcm == 1:
            return num
        else:
            found_lcm = 1
        num += upper_limit
  
start = time.time()

print(find_lcm(1, 20))

end = time.time()

print(f"runtime: {end-start}")