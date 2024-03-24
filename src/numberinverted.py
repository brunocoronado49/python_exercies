def number_inverted(number):
    result = ''
    str_number = str(number)
    
    for i in range(len(str_number) -1, -1, -1):
        result += str_number[i]
        
    return int(result)

print(number_inverted(321))
print(number_inverted(789))