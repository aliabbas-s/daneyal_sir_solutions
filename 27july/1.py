# PF-Assgn-47
#PF-TCV-Assgn-47

def encrypt_sentence(sentence):
    sample_list = sentence.split()
    s = []
    vowel_stack = []
    conso_stack = []
    vowel = ["a", "e", "i", "o", "u"]
    for i in range(len(sample_list)):
        if i % 2 == 0:
            s.append(sample_list[i][::-1])
        else:
            for j in sample_list[i]:
                if j.lower() in vowel:
                    vowel_stack.append(j)
                else:
                    conso_stack.append(j)

            ans = conso_stack + vowel_stack
            s.append("".join(ans))
            vowel_stack =[]
            conso_stack = []
    ans = " ".join(s)
    return ans


sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)