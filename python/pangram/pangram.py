def is_pangram(sentence):
    sentence = set(sentence.lower())
    for num in range(97,123):
        if chr(num) not in sentence:
            return False
    return True