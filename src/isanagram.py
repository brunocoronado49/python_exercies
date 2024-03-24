def is_anagram(word_one, word_two):
    if word_one == word_two: return False
    
    if len(word_one) != len(word_two): return False
    
    list_letters_one = list(word_one)
    list_letters_two = list(word_two)
    
    if sorted(list_letters_one) == sorted(list_letters_two):
        return True
    
    return False


print(is_anagram('silent', 'listen'))
print(is_anagram('dog', 'cat'))