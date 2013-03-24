words_f = open('wordsEn.txt', 'r')
print ','.join([x.strip() for x in words_f.readlines() if sum([ord(i)-96 for i in x.strip()])==100])
words_f.close()
