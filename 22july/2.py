#account_number = int(input())
#account_balance = int(input())
#salary_loan_type = input().lower()
#loan_amount_expected = int(input())
#customer_emi_expected = int(input())

account_number = 1200
account_balance = 120000
salary = 50000
loan_type = "car".lower()
loan_amount_expected = 7500000
customer_emi_expected = 35

if len(str(account_number)) == 4 and str(account_number)[0] == "1" and account_balance >= 100000:
    if salary > 25000 and loan_type == "car":
        eligible_loan_amount = 500000
        emi = 36
    if salary > 50000 and loan_type == "house":
        eligible_loan_amount = 6000000
        emi = 60

    if salary > 75000 and loan_type == "business":
        eligible_loan_amount = 7500000
        emi = 84
    if loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= emi:
        print("Acc No.-",account_number)
        print("Eligible Loan Amount-",eligible_loan_amount)
        print("Requested Loan amount-",loan_amount_expected)
        print("Eligible EMI-", emi)
        print("Requested EMI-", customer_emi_expected)
    else:
        print("Invalid Data")



