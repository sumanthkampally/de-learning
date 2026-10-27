
count = 1
while count<=3:
    print(count)
    count+=1
print("done")

n = 10
while n > 0:
    print(n)
    n-=4
print("end")

correct_password = "data123"
attempts = 0

while attempts < 3:
    password = input("Enter the password: ")
    attempts += 1
    if password == correct_password:
        print("Access granted")
        break
    print("Wrong password")
print("Finished")

total = 0
number = 1
while total < 10:
    total += number
    number += 1
print(total, number)

customer = {"name": "Sam", "city": "Toronto", "age": 30}
print(customer)
print(customer["name"])
print(customer["age"])
print(len(customer))
print(customer.get("email"))
print(customer.get("email", "not provided"))

customer["email"] = "sam@example.com"
customer["age"] = 31
del customer["city"]
print(customer)

print("name" in customer)
print("city" in customer)


customer = {"name": "Sam", "city": "Toronto", "age": 30}

for key in customer:
    print(key)

for key, value in customer.items():
    print(f"{key}: {value}")


orders = [
    {"order_id":"a1", "price":20.0},
    {"order_id":"a2", "price":55.5},
    {"order_id":"a3", "price":12.25},
]

total = 0
for order in orders:
    total +=order["price"]
print(total)


stock = {"apple": 5, "banana": 0, "cherry": 12}
in_stock = []
for item, quantity in stock.items():
    if quantity > 0:
        in_stock.append(item)
print(in_stock)

count = 5
while count >= 1:
    print(count)
    count -= 1
print("Liftoff!")


total = 0
while True:
    number = int(input("Enter a whole number (0 to stop:"))
    if number == 0:
        break
    total += number
print(total)


products = {"name":"Watch","price":25,"stock":20}
products["price"] = 35
products["category"] = "Accessories"
for key,value in products.items():
    print(f"{key}: {value}")

counts = {}
words = ["a", "b", "a", "c", "b", "a"]
for word in words:
    if word in counts:
        counts[word] = counts[word]+1
    else:
        counts[word] = 1
print(counts)


students = [
    {"name": "Ana", "score": 82},
    {"name": "Ben", "score": 45},
    {"name": "Cara", "score": 67},
]
total = 0
passed = []
for student in students:
    total += student["score"]
    if student["score"] >=50:
        passed.append(student["name"])
average = total/len(students)
print(f"{average:.1f}")
print(passed)