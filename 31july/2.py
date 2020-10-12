from itertools import permutations
start=1
end =100
for i in range(start,end+1):
    num = i
    digit = len(str(i))
    count = 0
    prod = 1
    li = []
    count_primes=0
    powTen = pow(10, digit - 1)
    print(num,end=" ")

    for i in range(digit - 1):
        firstDigit = num // powTen

        # formula to calculate left shift
        # from previous number
        left = (num * 10 + firstDigit -
                (firstDigit * powTen * 10))
        for i in range(1,left):
            if left % i==0:
                count = count + 1
            if count == 2:
                li.append(1)
        num = left
    for i in li:
        prod = prod*i
    if prod == 1:
        count_primes= count_primes + 1
print(count_primes)