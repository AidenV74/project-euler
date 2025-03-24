def num_to_word(limit):
    
    #strings
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    others = ["hundred", "thousand", "million"]
    
    nums = []

    #numbers 0 - 9
    def num_to_word_ones(num):

        word_num = ones[int(num)]
        return word_num
    #numbers 10 - 99
    def num_to_word_tens(num):
        
        #11 - 19
        if int(num) < 20 and int(num) != 10:
            word_num = teens[int(num) - 11]
        #21 - 99, not including 10, 20, 30, etc.
        elif int(num) > 19 and num[1] != "0":
            word_num = tens[int(num[0]) - 1] + ones[int(num[1])]
        #10, 20, ... 90
        else:
            word_num = tens[int(num[0]) - 1]
        
        return word_num
    #numbers 100 - 999        
    def num_to_word_hundreds(num):
        
        #ones
        if int(num[1] + num[2]) < 10 and num[2] != "0":
            word_num = ones[int(num[0])] + others[0] + "and" + num_to_word_ones(num[2])
        #tens
        elif int(num[1] + num[2]) >= 10:
            word_num = ones[int(num[0])] + others[0] + "and" + num_to_word_tens(num[1] + num[2]) 
        #one hundred, two hundred, etc.
        else:
            word_num = ones[int(num[0])] + others[0]

        return word_num
    #numbers 1000 - 9999
    def num_to_word_thousands(num):
        
        #ones
        if int(num[2] + num[3]) < 10 and num[3] != "0":
            word_num = ones[int(num[0])] + others[1] + "and" + num_to_word_ones(num[3])
        #tens
        elif int(num[2] + num[3]) >= 10 and int(num[1]) == 0:
            word_num = ones[int(num[0])] + others[1] + "and" + num_to_word_tens(num[2] + num[3])
        #hundreds
        elif int(num[1]) > 0:
            word_num = ones[int(num[0])] + others[1] + num_to_word_hundreds(num[1] + num[2] + num[3])
        #one thousand, two thousand, etc.
        else:
            word_num = ones[int(num[0])] + others[1]
        
        return word_num
    
    for i in range(1, limit + 1):
        num = str(i)
        if len(num) == 1:
            nums.append(num_to_word_ones(num))
        elif len(num) == 2:
            nums.append(num_to_word_tens(num))
        elif len(num) == 3:
            nums.append(num_to_word_hundreds(num))
        elif len(num) == 4:
            nums.append(num_to_word_thousands(num))
    
    print(nums)
    lengths = [len(number) for number in nums]
    print(lengths)
    return sum(lengths)

    
print(num_to_word(1000))

    