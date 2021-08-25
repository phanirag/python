#Tuple it is immutable list
tup = (1,2,3,4,5)
#tup[0] = 3 # throws error
# cannot sort or reversed which incresses performance

print(tup.count(1))
print(tup.index(5))

x,y,z,*o = (1,2,3,4,5,6)
print(x)
print(y)
print(z)
print(o)
