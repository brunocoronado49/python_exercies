def is_anagram(first_word, second_word):
    if first_word == second_word: return False
    if len(first_word) != len(second_word): return False
    
    letter_first_word = list(first_word).sort()
    letter_second_word = list(second_word).sort()
    
    if letter_first_word == letter_second_word:
        return True
    
    return False
    

print(is_anagram('silent', 'listen'))
print(is_anagram('mariano', 'mariana'))
print(is_anagram('hola', 'laoh'))
print(is_anagram('juan', 'perez'))