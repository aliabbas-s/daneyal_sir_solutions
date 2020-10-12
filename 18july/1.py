input_string = input("Enter string")
dict = {}
li = []
li2= []
count = 0
for i in range(len(input_string)):
    if input_string[i] not in li:
        li.append(input_string[i])
for i in range(len(li)):
    count = input_string.count(input_string[i])
    li2.append(count)
for i in range(0,len(li)):
    dict[li[i]]= li2[i]
print(li)
print(li2)
print(dict)



