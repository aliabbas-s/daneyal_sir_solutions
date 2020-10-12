# PF-Tryout
import random

x = 200
head = 0
tail = 0
for i in range(x + 1):
    draw = random.randint(1, 2)
    if draw == 1:
        head = head + 1
    else:
        tail = tail + 1
    c = random.randint(67, 70) / 100 * x

    head = head + (c - head)
    tail = x - head
print("heads = ", head)
print("tails = ", tail)
