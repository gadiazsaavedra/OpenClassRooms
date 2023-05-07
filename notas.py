# sourcery skip: avoid-builtin-shadow
colors = ["red", "yellow", "orange", "green", "blue"]
print(colors)
colors[3] = "emerald"
print(colors)
for color in colors:
    print(color)
list = [7, 5]
print(list)
list.insert(1, 12)
print(list)
list[0] = 4
print(list)
list.remove(12)
print(list)
print(list.index(5))
list.extend([1, 2, 3])
print(list)
del list[3]
print(list)
print(len(list))
guests = ["Joey", 'Martin', 'Mary']
print(guests)
print(len(guests))
guests[1] = "John"
print(guests)
guests.remove("Joey")
print(guests)
for guest in guests:
    print(guest)
accounts = {'mariana': '123', 'jose': '456', 'pedro': '789'}
print(accounts)
print(accounts['mariana'])
name = input('what is your name, dear stranger ? ')
if len(name) > 0:
    print(f'hello, {name}')
else:
    print('hello, stranger')
