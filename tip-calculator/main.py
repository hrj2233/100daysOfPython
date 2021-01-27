bill = float(input("Please enter the amount to be paid. $"))

people = int(input("Please enter the number of people to pay. "))

tip = int(input("Please enter the percentage of tips to be paid. 10, 12, or 15? "))

pay_per_person = round((bill / people) * (1 + (tip / 100)),2)

print(f"Each person should pay: ${pay_per_person}")