age= int(input("Enter age"))
health = "excellent"
lives_where = "city"
answer = True
sex = "male"

if age >= 25 and age <=35:
    if sex == "male":
        if health == "excellent" and lives_where == "city":
            premium = "4/Thousand"
            policy_exceed_limit = "2lakhs"
        elif health == "poor" and lives_where == "village":
            policy_exceed_limit = "10,000"
        else:
            answer = False
    elif sex == "female":
        if health == "excellent" and lives_where == "city":
            premium = "3/thousand"
            policy_exceed_limit = "1lakh"
        else:
            answer = False
    else:
        answer = False
if answer == True:
    print("Premium = ",premium,"\nPolicy exceed limit =",policy_exceed_limit)
elif answer == False:
    print("Policy cant be Insured")


