l = [1,2,2,3,4,4,4,10]

count = 0
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        count+=1
print(count)