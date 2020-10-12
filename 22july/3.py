type_of_food = "V".lower()
no_of_plates = 4
distance = 15
if type_of_food == "v":
    cost_of_plate = 120
elif type_of_food == "n":
    cost_of_plate = 150
if distance <= 3:
    charge = 0*distance
elif distance > 3 and distance < 6:
    charge = 0*3 + (distance-3)*3
elif distance > 6:
    charge = 0*3 + 3*6 + (distance-9)*6
if type_of_food == "v" or type_of_food == "n":
    if distance > 0:
        if no_of_plates >= 1:
            bill = (cost_of_plate * no_of_plates)+charge
        else:
            bill = -1
    else:
        bill = -1
else:
    bill = -1

print(bill)