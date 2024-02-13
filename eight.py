def fibonacci(number):
    a = 0
    b = 1
    
    print(f' {a} {b} ')
    
    for i in range(number):
        next = a + b
        print(f' {next} ')
        a = b
        b = next


fibonacci(50)