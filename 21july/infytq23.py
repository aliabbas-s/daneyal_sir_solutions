# PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    bill_amount = -1
    price_of_gem = {}

    for i in range(len(gems_list)):
        price_of_gem[gems_list[i]] = price_list[i]

    customer_dict = {}
    bill = 0
    for i in range(len(reqd_quantity)):
        customer_dict[reqd_gems[i]] = reqd_quantity[i]
    for i in range(len(reqd_gems)):
        if reqd_gems[i] not in gems_list:
            return bill_amount

    for i, j in price_of_gem.items():
        for m, n in customer_dict.items():
            if m.lower() == i.lower():
                bill = bill + (n * j)
    if bill > 30000:
        bill_amount = bill - ((5 / 100) * bill)
    else:
        bill_amount = bill
    return bill_amount


# List of gems available in the store
gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]

# Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list = [1760, 2119, 1599, 3920, 3999]

# List of gems required by the customer
reqd_gems = ["Ivory", "Emerald", "Garnet"]

# Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity = [3, 10, 12]

bill_amount = calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)