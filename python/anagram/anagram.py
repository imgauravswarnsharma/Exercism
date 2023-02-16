def find_anagrams(word, candidates):
    list_x = []
    dict_word = {}

    for char in word.lower():
        if char in dict_word:
            dict_word[char] += 1
        else:
            dict_word[char] = 1

    for words in candidates:
        if word.lower() == words.lower():
            continue
        dict_words = {}
        for char in words.lower():
            if char in dict_words:
                dict_words[char] +=1
            else:
                dict_words[char] =1
        if dict_words== dict_word:
            list_x.append(words)
    return list_x