# Write a python program to print on a line, the nth prime and the nth prime of the form 3x + 1
# Continue printing until the user presses Ctrl+C
# Eg:
# 2 7
# 3 13
# 5 19
# ....
def prime_generator():
    prev_primes = []
    def is_prime(item):
        for i in prev_primes:
            if item%i == 0:
                return False
        prev_primes.append(item)
        return True
        
    item = 2
    while item < 100:
        if is_prime(item):
            yield item
        item += 1
        
def prime_3x_plus_one():
    for item in prime_generator():
        if (item-1) % 3 == 0:
            yield item
        item += 1
        
#for prime in prime_generator():
#    print ("{} - {}".format(prime, prime*3 + 1))
for prime, prime3x in zip(prime_generator(), prime_3x_plus_one()):
    print (prime, prime3x)
    
def multiple(item, number):
    pass
        