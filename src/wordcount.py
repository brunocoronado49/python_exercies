def word_count(word):
    list_old = word.split()
    list_words = []
    
    for i in list_old:
        if i not in list_words:
            list_words.append(i)
    
    return [list_words, len(list_words)]
    

print(word_count('pepe pica papas peladas pepe papas'))