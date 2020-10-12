from itertools import groupby

def medics(sample_input,sample_dict):
    key = []
    value = []
    answer = []
    max = 0
    for i in range(len(sample_input)):
        if i % 2 == 0:
            key.append(sample_input[i])
        else:
            value.append((sample_input[i]))
    value.sort()
    ans = groupby(value)
    for i in ans:
        answer.append((list(i[1])))
    for i in answer:
        if max < len(i):
            max = len(i)
            expected_output = i[0]
    return sample_dict[expected_output]


sample_input =[101,"P",102,"O",302,"P",305,"P",108,"O",109,"O"]
sample_dict = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
print(medics(sample_input,sample_dict))