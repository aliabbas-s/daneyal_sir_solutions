#PF-Tryout
import random
def guess_number(number_in_mind):
    x = random.randint(1,10)
    if number_in_mind == x:
        print("You have got it right!!!")
    elif number_in_mind < x:
        print("Number is low")
    else:
        print("Number is high")

#use the print statements given below wherever applicable
#print ('Number is low')
#print ('Number is high')
#print ('You have got it right!!!')

#Provide different values for number_in_mind and test your program
guess_number(4)