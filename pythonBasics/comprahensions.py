#Insted of looping a appending we can use comprehensions.
#List
my_list = [val for val in [1, 2, 3, 4, 5]]
print(my_list)
my_list = [char for char in "helloword"]
print(my_list)
my_list = [n * 2 for n in range(0, 10)]
print(my_list)
my_list = [n * 2 for n in range(0, 10) if n % 2 == 0]
print(my_list)

#Set
my_list = {val for val in [1, 2, 3, 4, 5]}
print(my_list)
my_list = {char for char in "helloword"}
print(my_list)
my_list = {n * 2 for n in range(0, 10)}
print(my_list)
my_list = {n * 2 for n in range(0, 10) if n % 2 == 0}
print(my_list)

#Dictonary
s_d = {'a': 1, 'b': 2}
my_dict = {k: v**2 for k, v in s_d.items()}
print(my_dict)

#find duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
