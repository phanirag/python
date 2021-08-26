#Conditonal Logic

#if,else,elif condition

is_old = False
is_new = True
if is_old:
    print('yes it is old')
elif not is_old and is_new:
    print('else if block')
else:
    print('no not old')
print('outside the block')

#Truthy and Falsy
#https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

is_old = 'hello'
is_new = 5
print(bool(is_old))
print(bool(is_new))
print(bool(0))
print(bool(None))
print(bool(0.0))
print(bool({}))
print(bool(''))
if is_old:
    print('yes it is old')
elif not is_old and is_new:
    print('else if block')
elif is_old or is_new:
    print('else if block')
else:
    print('no not old')
print('outside the block')

#Ternary Operator

is_friend = False
can_message = "can_message" if is_friend else "no message"
print(can_message)

#logical Operators

# < > >= <= == != and or not

# is vs ==
# == checks for the value
# is checks for the memory of the value

print(True == 1)
print('1' == 1)
print([] == 1)
print(10 == 10.0)

# print(True is True)
# print('1' is '1')
# print([] is []) # 2 list are located in different locations
# print(10 is 10.0)

# for loop

for items in 'hello world':
    print(items)

for items in [1, 2, 3, 4, 5]:
    print(items)

for items in {1, 2, 3, 4, 5}:
    print(items)

for items in (1, 2, 3, 4, 5):
    print(items)

for items in '*' * 10:
    print(items)

for items in range(1, 10):
    print(items)

for i in range(1, 11):
    for j in range(1, 11):
        print('*' * j)

#iterable -list,dictonary, tuple, set, string

users = {'hello': 'hello', 'age': 1, 'bool': True}

for k, v in users.items():
    print(k)
    print(v)

for item in users.values():
    print(item)

for item in users.keys():
    print(item)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for l in lst:
    v += i
print(v)

for _ in range(1, 10, 2):
    print(_)

for _ in range(10, 0, -1):
    print(list(range(3)))

#enumarate (if we want index) wroks with list, set, string, tuples
for i, char in enumerate("hello world"):
    print(i, char)

for i, char in enumerate(list(range(10))):
    if char == 3:
        print(f'index of {i}')

#While loop
#break - breaks the loop and gets out open
#continues - will ignore below code and loop again
i = 0
while i < 10:
    i += 1
    print(i)
else:
    print("done")

while True:
    response = input('yes/no:')
    if response == 'no':
        break

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 1, 0, 0, 0]]

for image in picture:
    for pixel in image:
        if (pixel):
            print('*', end="")
        else:
            print(' ', end="")
    print('')
