def findMultiples(num1, num2, rng):
    mults = []
    
    #loops through all numbers from 1 to the specified limit and multiplies the base number to find all multiples
    for i in range(1, rng):
        
        #adds product to list if not over range and not already in list
        if num1 * i < rng and num1 * i not in mults:
            mults.append(num1 * i)
        if num2 * i < rng and num2 * i not in mults:
            mults.append(num2 * i)
            
    return mults

print(sorted(findMultiples(3, 5, 1000)))
print("Sum: " + str(sum(findMultiples(3, 5, 1000))))