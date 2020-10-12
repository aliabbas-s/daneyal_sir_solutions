customer_details = {1001:"John",1004:"Jill",1005:"Joe",1003:"Jack"}

#Print details of customers
for i,j in customer_details.items():
    print(i,"-",j)

#Print customers
print()
x = len(list(customer_details.values()))
print("number of customers :",x)

#print customerr names in ascending order
print()
names = (list(customer_details.values()))
names.sort()
print(names)

#delete the details of customer with customer id = 1005
dict ={}
for i,j in customer_details.items():
    if i != 1005:
       dict[i] = j
print(dict)
"""
customer_details.pop(1005)
print(customer_details)
"""

#E -update the dictioanry value
customer_details[1003] = "Mary"
print(customer_details)

#F - check whether detaiils of cutomer d 2002 exits in the dictionary
count = 0
for i,j in customer_details.items():
    if i == 1002:
        count += 1
if count == 1:
    print("It Exists")
else:
    print("It dosent")