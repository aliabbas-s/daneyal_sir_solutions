sample_Input = input("Enter a string").upper()
li = []

for i in range(len(sample_Input)):
    if sample_Input[i] not in li:
        li.append(sample_Input[i])
for i in range(len(li)):
    count = sample_Input.count(li[i])
    print(str(count)+li[i])