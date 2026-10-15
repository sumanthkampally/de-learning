name = input("Enter the username ")
city = input("Enter the city name ")
print(name + " lives in " + city)
print(f"{name} lives in {city}")


first_number = float(input("Enter first number= "))
second_number = float(input("Enter second number= "))
total = first_number + second_number
average = total/2
print("Sum is",total)
print(f"sum is {total:.2f}")
print("Average is",average)
print(f"average is {average:.2f}")

price = float(input("Enter the Price= "))
tax = price * (13/100)
total = price+tax
print("Total Price",round(total,2))


name = input("Enter the username ")
city = input("Enter the city name ")
print(f"{name} lives in {city}")

first_number = float(input("Enter first number= "))
second_number = float(input("Enter second number= "))
total = first_number + second_number
average = total/2
print(f"sum is {total:.2f}")
print(f"average is {average:.2f}")
              

text = input("Enter a sentence ")
print(text.strip())
print(text.upper())
print(text.title())
print(len(text))

email = (input("Enter the email address ")).strip().lower()
print(email.endswith(".com"))