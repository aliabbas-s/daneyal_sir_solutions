x = "An apple a day keeps the doctor away"
x = "".join(x.split())
resultant_string = x[::2]
expected_output = resultant_string[::-1]
print(expected_output)