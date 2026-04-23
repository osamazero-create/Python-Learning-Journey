name = input("Enter your name: ")
age = input("Enter your age: ")
destination = input("Enter destination (Cairo, Dubai, London): ")
tickets = int(input("How many tickets: "))
businessClass = input("Do you want business class? (yes/no): ")
discountCode = input("Enter discount code: ")

price = 0
if destination == "Cairo":
    price = 200
if destination == "Dubai":
    price = 400
if destination == "London":
    price = 600
subtotal = price * tickets
extraCharge = 0
if businessClass == "yes":
    extraCharge = (price * 0.5) * tickets
    subtotal = subtotal + extraCharge

discountValue = 0
if discountCode == "SAVE10":
    discountValue = subtotal * 0.1
    subtotal = subtotal - discountValue

tax = subtotal * 0.14
finalTotal = subtotal + tax

print("Name: " + name)
print("Age: " + age)
print("Destination: " + destination)
print("Tickets: " + str(tickets))
print("Base Price: " + str(price * tickets))
print("Business Extra: " + str(extraCharge))
print("Discount: " + str(discountValue))
print("Tax: " + str(tax))
print("FINAL TOTAL: " + str(finalTotal))