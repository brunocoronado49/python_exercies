import math

def prime_number(num):
    if num <= 1: return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True


def main(num):
    for i in range(num):
        if prime_number(i):
            print(f'{i} is prime number')
        else:
            pass


main(50)