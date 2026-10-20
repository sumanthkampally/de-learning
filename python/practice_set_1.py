
# Q1
price = 49.99
quantity = 3
total_cost = price * quantity
print(f"{total_cost:.2f}")
# Q2
first_number = int(input("print a first number:"))
second_number = int(input("print a second number:"))
total = first_number+second_number
difference = first_number-second_number
product= first_number*second_number
whole_division = first_number//second_number
remainder = first_number % second_number
print(f"Sum: {total}, Difference: {difference}, Product: {product}, "
      f"Whole division: {whole_division}, Remainder: {remainder}")

# Q3
name =input("Enter a full name:").strip().title()
print(name)
print("no_of_characters:",len(name))

# Q4
name = input("Enter a name:").title().strip()
city = input("Enter a city:").title().strip()
age =int(input("Enter a age:"))
print(f"{name} is {age} years old and lives in {city}.")
print(f"Next year: {age + 1}")

# Q5

number = float(input("Enter a number:"))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is equal to zero.")

#Q6

year = int(input("Enter a year:"))
if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Q7
total_amount = float(input("Enter a order total:"))
if total_amount >= 100:
    shipping_cost = 0
elif total_amount >= 50:
    shipping_cost = 5
else:
    shipping_cost = 10
final_total = shipping_cost+total_amount
print(f"{shipping_cost:.2f} is shipping cost and {final_total:.2f} is final total")

#Q8
my_list = [1,10,3,4,6,39]
print("first number: ", my_list[0])
print("last  number: ", my_list[-1])
print("no. of characters: ", len(my_list))
print("Sum of numbers: ", sum(my_list))
print("average of numbers: ",round(sum(my_list)/len(my_list),2))
print("differece of max_num and min_num: ",max(my_list)-min(my_list))

#Q9
names = ["ana", "ben", "carl", "dee"]
names.append("eli")
names.insert(0,"zoe")
names.remove("carl")
print(names)
print(len(names))

#Q10
number1=[2,3,4,6,7,8,9,5]
print(number1[:3])
print(number1[-3:])
print(number1[1:-1])

#Q11

available_products = ["iphone","headset","watch","television"]
product = input("Enter a product:").strip().lower()
if product in available_products:
    print(f"{product} is In stock")
else:
    print(f"{product} is out of stock")

#Q12
first_score = float(input("Enter a first_score: "))
second_score = float(input("Enter a second_score: "))
third_score = float(input("Enter a third_score: "))
average_score = (first_score+second_score+third_score)/3
if average_score >= 90:
    grade = "A"
elif average_score >=75:
    grade = "B"
elif average_score >=50:
    grade = "C"
else:
    grade = "F"
print(f"Average: {average_score:.1f} - Grade {grade}")