def translate(text):
    text_list = text.split(" ")
    vowel = 'a','e','i','o','u','xr','yt'
    print(text_list)
    result_list = []

    for words in range(len(text_list)):
        temp = text_list[words]
        if temp.startswith(vowel):
            result_list.append(temp+'ay')
        else:
            not_vowel = ""
            n = 0
            for char in temp:
                if char not in vowel:
                    not_vowel +=char
                    n +=1
                    if n>1:
                        if char =='y':
                            break
                else:
                    break

            #Actual substring creation starts now based on not_vowel length
            if len(temp) ==2:
                if temp[1] == 'y':
                    result_list.append(temp[::-1]+'ay')
                    continue
            if 'qu' in temp:
                result_list.append(temp[n+1:]+temp[:n+1]+'ay')
                continue
            if temp[n-1] =='y' and n>1:
                result_list.append(temp[n-1:]+temp[:n-1]+'ay')
                continue
            result_list.append(temp[n:]+temp[:n]+'ay')

    return " ".join(result_list )

# Alternate Solution using sets and slices
'''
VOWELS = {"a", "e", "i", "o", "u"}
VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
SPECIALS = {"xr", "yt"}


def translate(text):
    piggyfied = []

    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            piggyfied.append(word + "ay")
            continue

        for pos in range(1, len(word)):
            if word[pos] in VOWELS_Y:
                pos += 1 if word[pos] == 'u' and word[pos - 1] == "q" else 0
                piggyfied.append(word[pos:] + word[:pos] + "ay")
                break

    return " ".join(piggyfied)
'''