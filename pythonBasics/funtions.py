#Functions

#clean code


def is_even_or_odd(num):
    return num % 2 == 0


print(is_even_or_odd(55))


def first_fun(name="default", emoji=":)"):
    print(f"hello {name} , {emoji}")


def find_duplicates(some_list):
    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    print(duplicates)


picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 1, 0, 0, 0]]


def show_pic():
    for image in picture:
        for pixel in image:
            if (pixel):
                print('*', end="")
            else:
                print(' ', end="")
        print('')


find_duplicates(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'])
first_fun('phani', ":P")
show_pic()

#keyword aurgment
first_fun(emoji=":>", name='asdad')
first_fun()


#return functions
def sum(a, b):
    def another_sum(a, b):
        return a + b

    return another_sum(a, b)


val = sum(1, 2)
print(val)


# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
def checkDriverAge():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge()


#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.
def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too yound to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge()
