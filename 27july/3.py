#PF-Exer-34
import math
def find_number_of_combination(number_of_flavours):
    total_combination=0
    for i in range(number_of_flavours):
        total_combination = total_combination +(math.factorial(number_of_flavours))/((math.factorial(i))*(math.factorial(number_of_flavours-i)))
    total_combination = total_combination + 1
    return total_combination


#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(6)
print(number_of_combination)