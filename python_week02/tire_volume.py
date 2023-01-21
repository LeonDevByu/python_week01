# 02 Prove: Calling Functions
# NAME: EDWIN LEONARDO LEON MATIAS

import math
from datetime import datetime

w = int(input("Enter the width of the tire in mm (ex 205):"))
a = int(input("Enter the aspect ratio of the tire (ex 60):"))
d = int(input("Enter the diameter of the wheel in inches (ex 15):"))

v = (math.pi * w * w * a * (w * a + 2540 * d)) / 10000000000
current_date_and_time = datetime.now()

print()
print("==================Data for printing===================")
print()

# Optional data to display in the console before printing:
print(f"width of the tire in mm: {w}")
print(f"aspect ratio of the tire: {a}")
print(f"diameter of the wheel in inches: {d}")
print(f"The approximate volume is {v:.2f} liters")
print()
print(f"Current date: {current_date_and_time:%Y-%m-%d} ------- Hour: {current_date_and_time:%H:%M:%S}")

with open("volumes.txt", "at") as volume_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f} ....... {current_date_and_time: %H:%M:%S}",
          file=volume_file)

# Exceeding the Requirements
# the program asks the user if she wants to buy tires with the
# dimensions that she entered. If the user answers “yes”, the program
#asks for her phone number and stores her phone number in the volumes.txt file.

k = input("You want to buy tires with the dimensions you entered(YES or NO):")
if k == "yes":
    phone: str = input("Please enter phone number: ")
    print("Thank you so much, Thank you very much, we will be contacting you! ")
    with open("volumes.txt", "at") as volume_file:
        print(f"Phono number: {phone}", file=volume_file)
else:
    print("Thank you so much, goodbye ")

