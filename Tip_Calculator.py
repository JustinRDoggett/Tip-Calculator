print("Welcome to the tip calculator program!")
bill_amount = float(input("Enter the cost of the meal: "))
people = int(input("How many people are going to split the bill? "))
tip = float(input("Enter the tip percentage for the meal: "))

bill_including_tip = bill_amount * tip
total_cost_of_meal = bill_amount + bill_including_tip
price_per_person = (bill_amount / people) * tip

# formatting total amount to two decimal places
price_rounded = "{:.2f}".format(price_per_person)
print(f"The cost of the meal is {bill_amount}. The cost of the meal including tip is {bill_including_tip}. With the bill split between {people} people, each person should pay {price_rounded}.")