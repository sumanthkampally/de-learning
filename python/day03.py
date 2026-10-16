"""
age = 20
print(age > 18)
print(age == 20)
print(age != 21)
print(age <= 10)

age = int(input("ENter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower().strip()

if age >= 18 and has_ticket == "yes":
    print("Welcome in")
else:
    print("Sorry, cannot enter")
   
"""
number = int(input("Enter a whole number: "))
if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")
score = int(input("Enter a score:"))
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Grade F")

price = float(input("Enter a price:"))
if price > 100:
    tax_rate = 0.15
elif price > 50:
    tax_rate =  0.13
else:
    tax_rate = 0.05

total = price *(1+tax_rate)
print(f"total price is {total:.2f}")


correct_password = "data123"
password = input("Enter the password:")
if correct_password == password:
    print("Access Granted")
else:
    print("Access Denied")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a>=b and a>=c:
    print(f"{a} is the largest")
elif b>=c and b>=a:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")