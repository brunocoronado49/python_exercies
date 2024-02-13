def same_vocal(word):
    VOCALS = ['a', 'e', 'i', 'o', 'u']
    first_letter = word[0]
    last_letter = word[-1]
    
    if first_letter in VOCALS and last_letter in VOCALS and first_letter == last_letter:
        return True
    return False


print(same_vocal('maria'))
print(same_vocal('miriam'))
print(same_vocal('anna'))
print(same_vocal('eduarde'))