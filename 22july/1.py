x = [10, 20, 30, 40, 30, 20]
count = 0
for i in range(0,len(x)-1):
    if x[i] == x[i+1]:
        count+=1
print(count)