def fizz_buzz(number):
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzBuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)
            

fizz_buzz(100)