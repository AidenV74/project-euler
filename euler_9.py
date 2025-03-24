#FUNCTIONS
def find_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            
            c = (a**2 + b**2) ** 0.5
            
            if c % 1 == 0 and a<b<c and a+b+c==1000:
                print(a, b, int(c))
                print(int(a*b*c))
                
#MAIN          
limit = 1000
find_pythagorean_triples(limit)