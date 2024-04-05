distance = 16

if distance < 3:
    mode_of_travel = "Walk"
elif distance < 16:
    mode_of_travel = "Bike"
else:
    mode_of_travel = "Car"

print("Distance is",distance,"km and you can choose",mode_of_travel,"as your mode of transport!")