
numbers = [1, 2, 3]
for n in numbers:
    print(n * 10)
print("finished")

for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(0,10,2):
    print(i)


numbers = [20, 45, 23, 10]
total = 0
for n in numbers:
    total = total + n
print(total)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
    print(total)
print("done:", total)


numbers = [20, 45, 23, 10, 2, 15]
count = 0
for n in numbers:
    if n > 15:
        count += 1
print(count)


scores = [55, 80, 90, 40, 75]
passed = 0
total = 0
for score in scores:
    if score >= 50:
        passed += 1
        total += score
print(passed)
print(total)


cities = [" Toronto", "  montreal", "VANCOUVER  "]
clean_cities = []
for city in cities:
    clean_cities.append(city.strip().lower())
print(clean_cities)

prices = [19.99, 5.50, 120, 45, 80.25]
expensive = []
for price in prices:
    if price > 50:
        expensive.append(price)
print(expensive)


numbers = [3,8,12,5,20]
doubled = []
for n in numbers:
    doubled.append(n*2)
print(doubled)
print(numbers)

#Q1
for i in range(1,11):
    print(i)

#Q2
number = 0
for i in range(1,11):
    number = 7 * i
    print(f"7 x {i} = {number}")

#Q3
total = 0
for i in range(1,101):
    total += i
print(total)


#Q4
total = 0
count = 0
prices = [19.99, 5.50, 120, 45, 80.25]
for price in prices:
    total +=price
    if price >50:
        count += 1
print(f"Total is {total:.2f}")
print(f"no. of prices over 50 are {count}")

#Q5
cities = [" Toronto", "  montreal", "VANCOUVER  "]
clean_cities=[]
for city in cities:
    clean_cities.append(city.strip().lower())
print(clean_cities)


#Q6
number = [14, 3, 99, 27, 56]
largest = number[0]
for i in number:
    if i > largest:
        largest = i
print(largest)