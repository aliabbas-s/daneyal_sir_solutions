x = input("Enter a string").lower()
li = x.split(" ")
index_list = []
new_list = []
for i in range(len(li)):
    if li[i] == "not":
        index_list.append(i)
    if li[i] == "poor":
        index_list.append(i)

new_list =  li[0:index_list[0]]+["good"]+li[index_list[1]+1:]
print(" ".join(new_list))