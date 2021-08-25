#Strings are immutable.
print(type("hell"))
username = "super"
passd  = username +'pass'
print(passd)

#Long strings
string = '''
assert
asd2s
as2asd
asdad
'''
print(string)

#Escape Sequnce
print("It\'s \"Kind \" \n of sunny")
print('hello' + 'new')

#Type Covertion
print(type(str(100)))

#fomatted String
name = "phani"
user = "jhon"
age = 40
print("hello {0} ! My name is {1} and age is {2}".format(name, user,age))

print(f"hello {name} ! My name is {user} and age is {age}")



#String indexing

var = 'phaniraghava'
print(var[1])
#[start:stop:stepover]
print(var[1:5:2])
print(var[1:])
print(var[:3])
print(var[::2])
#revers indexing
print(var[-1]) 
#revers string
print(var[::-1])
#revers string with stepover
print(var[::-2])

#immutable we cannot reassigne we can change value.

var[2] = '2' #will not work 