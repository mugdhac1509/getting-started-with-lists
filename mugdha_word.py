def match_words(words):
    ctr = 0
    empty_list = []
    for word in words:
        if len(word) >1 and word[0] == word [-1]:
            ctr = ctr+1
            empty_list.append(word)

    print("List of words with first and last characters same",empty_list)
    return ctr 

count= match_words(['abc','cfc','xyz', 'aba', '1221'])

print(count)