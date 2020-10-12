def fact(num):
    prod = 1
    for i in range(1,num+1):
        prod = prod * i
    return prod

def strong(sample_list):
    sum = 0
    l2 = []
    for i in sample_list:
        s = str(i)
        for j in range(len(s)):
            sum = sum + fact(int(s[j]))
        if sum == i:
            l2.append(sum)
        sum = 0
    return l2

sample_list = [145,375,100,2,10]
print(strong(sample_list))