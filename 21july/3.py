price_of_gem = {"Emerald":1760,"Ivory":2119,"Jasper":1599,"Ruby":3920,"Garnet":3999}
discount = {"Ivory":3,"Ruby":4,"Others":6}
gem = ["Emerald","Ivory","Jasper","Ruby","Garnet"]
item_number = [3,2,0,0,7]
customer_dict ={}
answer_without_discount = []
for i in range(len(item_number)):
    customer_dict[gem[i]] = item_number[i]
for i,j in price_of_gem.items():
    for m,n in customer_dict.items():
        answer_without_discount.append(n*j)
sum1 = 0
for i,j in customer_dict.items():
    if j > 0:
        if i in list(discount.keys()):
            sum1 =sum1 + discount[i]
bill_amount = sum(answer_without_discount)-((sum1/100)*sum(answer_without_discount))
print(bill_amount)