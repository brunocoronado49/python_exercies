def reverse_string(word):
    result = ''
    
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
        
    return result


print(reverse_string('hello world'))