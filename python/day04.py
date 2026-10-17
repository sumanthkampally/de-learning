'''
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[-2])
print(fruits[2])
print(fruits[-1])
print(len(fruits))

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:2])
print(numbers[2:])
print(numbers[-2:])
print(numbers[0:3])
print(numbers[3:])
print(numbers[:-1])


items = ["a", "b", "c"]
items.append("d")
items.insert(0, "z")
items.remove("b")
print(items)
print(len(items))


scores = [72, 95, 88, 60]
print(sum(scores))
print(min(scores))
print(max(scores))
print(sum(scores) / len(scores))
print(88 in scores)
print(50 in scores)
scores.sort()
print(scores)


data = [4, 8, 15, 16, 23, 42]
print(sum(data))
print(sum(data) / len(data))
print(15 in data)
print(max(data) - min(data))

'''

myset = [20,45,23,10,2]
print(myset[0])
print(myset[-1])
print(len(myset))

city = ["mississauga","scarborough","whitby","ajax","orilla"]
city.append("seattle")
city.remove("ajax")
print(city)
print(len(city))

numbers = [20,45,23,10,2,15]
print(sum(numbers))
print(sum(numbers)/len(numbers))
print(max(numbers))
print(min(numbers))

print(numbers[:3])
print(numbers[-2:])
print(numbers[1:])

membership_city = ["mississauga","scarborough","whitby","ajax","orilla"]
city_name = input("enter a city name:").strip().lower()
print(city_name in membership_city)