def mergeAlternately(word1, word2):
    new_word = ""
    for i in range(min(len(word1), len(word2))):
        if i % 2 == 0:
            new_word = new_word + word1[i]
        else:
            new_word = new_word + word2[i]
    return new_word

word1 = "abc"
word2 = "pqr"

print(mergeAlternately(word1, word2))