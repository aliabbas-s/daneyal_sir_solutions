input_string = input("Enter String from user")
input_string = "".join(input_string.split(" "))
print("input_string- ",input_string)
resultant_string = ""
for i in range(len(input_string)):
    if i%2 == 0:
        resultant_string = resultant_string + input_string[i]
print("resultant_string- ",resultant_string)
expected_output = resultant_string[-1::-1]
print("expected_output- ",expected_output)