# PF-Assgn-56
from itertools import groupby


def max_frequency_word_counter(data):
    word = ""
    frequency = 0
    li_word = data.split()
    li_word.sort()
    di = {}
    count = 0
    ans = groupby(li_word)
    max1 = 0

    for i in ans:
        di[i[0]] = len(list(i[1]))
    value = list(di.values())
    keys = list(di.keys())
    print(di)
    for i,j in di.items():
        if max(value) == j:
            count+=1
            word = i
            frequency = j
    if count == 1:
        print(word,frequency)
    else:
        for i,j in di.items():
            if j == frequency:
                if max1 < len(i):
                    max1 = len(i)
                    word = i
        print(word,frequency)
data = "Courage is not the absence of but rather judgement that something else more important than fear"
max_frequency_word_counter(data)