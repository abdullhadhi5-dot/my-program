age = int(input("Enter your age: "))

if age < 12:
    price = 100
elif age >= 65:
    price = 150
else:
    price = 250

print("Final ticket price: ₹", price)