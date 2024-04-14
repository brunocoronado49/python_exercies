import random


def find_number(number):
    target = random.randint(1, number)
    prediction = 0
    
    while prediction != target:
        prediction = int(input(f'Please, enter a number between 1 and {number}: '))
        
        if prediction < target:
            print('This number is smaller, enter another')
        elif prediction > target:
            print('This number is bigger, enter another')
        
    print(f'Congratulations! The number was {target}')
        

if __name__ == '__main__':
    find_number(32)