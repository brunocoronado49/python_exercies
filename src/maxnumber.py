def max_numb(n1, n2, n3):
    max = 0
    
    if n1 > n2:
        max = n1
    else:
        max = n2
    
    if max > n3:
        return max
    else:
        return n3
    

print(max_numb(44, 18, 23))
