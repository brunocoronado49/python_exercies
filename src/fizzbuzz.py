def fizz_buzz(limit):
    if limit < 0 or limit > 100:
        print('Error in the range')
        return
    
    for i in range(limit):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('fizz')
        elif i % 3 == 0:
            print('buzz')
        else:
            print(i)
            

fizz_buzz(50)