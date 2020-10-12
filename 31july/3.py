

# PF-Assgn-58
def validate_credit_card_number(card_number):
    x = str(card_number)
    answer = []
    sum2 = 0
    sum_step1 = 0
    for i in range(len(x) - 2, -1, -2):
        a = int(x[i]) * 2
        if a > 9:
            step1 = list(str(a))
            for i in step1:
                sum_step1 = sum_step1 + int(i)
            answer.append(sum_step1)
            sum_step1 = 0
        if a < 9:
            answer.append(a)
    sum1 = sum(answer)
    for i in range(len(x) - 1, -1, -2):
        sum2 = sum2 + int(x[i])
    result = (sum1+sum2)%10 == 0
    return result


# start writing your code here


card_number = 4539869650133101  #   #1456734512345698 # #5239512608615007
result = validate_credit_card_number(card_number)
if (result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")