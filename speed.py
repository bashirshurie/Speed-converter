# This program  convers the speeds 10 kph through 150 kph (in 10 kph increment)  into mph
START_SPEED = 10            # starting speed
END_SPEED = 151             # ending speed
INCREMENT = 10              # Speed increment
CONVERSION_FACTOR = 0.6214  # Conversion factor

# Print the table headings.
print("---------------")
print("KPH\tMPH")
print("---------------")

# Print the speeds.
for kph in range(START_SPEED, END_SPEED, INCREMENT) :
    mph = kph * CONVERSION_FACTOR
    print(kph,"\t", format(mph, '.1f'))