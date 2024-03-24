def number_bigger(n1, n2, n3):
    number = 0
    
    if n1 > n2:
        number = n1
    else:
        number = n2
    
    if number > n3:
        return number
    else:
        return n3


print(number_bigger(3, 6, 9))