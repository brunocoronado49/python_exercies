def number_inverted(number):
    result = ''
    
    for i in range(len(number) -1, -1, -1):
        result += number[i]
        
    return int(result)

print(number_inverted('123'))