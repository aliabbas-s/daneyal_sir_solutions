#Assignment 30 Day4
#Have to do it!

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

size = int(input())
inp = input().lower().strip()
inp = "".join(inp.split(" "))
k = int(input())
count = 0

li = list(combinations(range(1, len(inp) + 1), k))
get = []
print(li)
for i in range(len(inp)):
    if inp[i] == "a":
        get.append(i + 1)
print(get)
answer = []
new = []
for i in range(len(li)):
    for j in range(len(get)):
        if  get[j] in li[i]:
            count+=1
            answer.append(i)
for i in answer:
    if i not in new:
        new.append(i)

print(len(new))
count = len(new)
average = count/len(li)
print("%.3f" % (count / len(li)))