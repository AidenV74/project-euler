import time

def collatz_sequence(limit):
    
    num = 0
    
    terms = []
    terms_memory = [0]
    lengths = [0]
    
    #loops through numbers under the limit and generates the collatz sequence for each one
    for i in range(2, limit + 1):
        num = i
        terms.append(num)
        while num > 1:
            if num % 2 == 0:
                num = int(num / 2)
                terms.append(num)
            else:
                num = (3 * num) + 1
                terms.append(num)
    
        #if the length of this sequence is longer than that current longest, remember it
        if len(terms) > max(lengths):
            lengths = [len(terms)]
            terms_memory = [terms]
        terms = []
    
    #prints out the maximum length found, the number found from, and the sequence generated from the number
    print("Maximum length: " + str(max(lengths)))
    print("Number: " + str(terms_memory[0][0]))
    print("Sequence: " + str(terms_memory))
    
    

limit = 100_000

start = time.time()

collatz_sequence(limit)

end = time.time()

print(f"
Runtime: {end-start} seconds")