def anagrams():

    print('Input:')
    text = input().lower().split()
    word_1 = text[0]
    word_2 = text[1]
    is_anagram = True

    for char in word_1:
        if char in word_2:
            word_2 = word_2.replace(char, "", 1)
    if len(word_2) > 0:
        is_anagram = False
    print('Output:')
    if is_anagram:
        return 'ANAGRAMS'
    else:
        return 'NOT ANAGRAMS'


def anagrams_test_signature(word_1, word_2):
    is_anagram = True

    for char in word_1:
        if char in word_2:
            word_2 = word_2.replace(char, "", 1)
    if len(word_2) > 0:
        is_anagram = False
    print('Output:')
    if is_anagram:
        return 'ANAGRAMS'
    else:
        return 'NOT ANAGRAMS'


print(anagrams())
