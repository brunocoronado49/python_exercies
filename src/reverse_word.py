def reverse_word(word):
    result = ''
    for letter in range(len(word) - 1, -1, -1):
        result += word[letter]
    
    return result


if __name__ == '__main__':
    word = input('Please, enter a word: ')
    result = reverse_word(word=word)
    print(result)