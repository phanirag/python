lis = [1,2,3,4,True,"hello"]
print(lis)
print(lis[-1])
print(type(lis))

#List slicing
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

amaz = [1,2,3,4,5]
amaz[0] = [6]
new_amaz = amaz
new_amaz[0] = 7
print(new_amaz)

basket = [1,2,3,4]

#append(value)
new_basket = basket.append(200)
print(new_basket)
print(basket)
new_basket = basket
print(new_basket)

#Insert(index, value)
basket.insert(0, 12)
print(basket)

#extend(collection values)
basket.extend([23,34,21,33])
print(basket)

#pop(index)
print('pop')
basket.pop() # Pop we give index
print(basket)
basket.pop(1) 
print(basket)

#removing(value)
basket.remove(12) #remove we give value
print(basket)

#clear()
basket.clear()
print(basket)

basket = [1,2,3,4,5,3,4,3]
#index(index, start, stop)
print(basket.index(3,0,4))

# in keyword
print(1 in basket)
print(10 in basket)
print('in' in 'stirn in the value in')

#count(object)
print(basket.count(3))
print("in the in ".count("in"))

#sort
#basket.sort()
print(sorted(basket))
print(basket)

#copy()
new_basket = basket[:]
new_basket.append(12233)
new_basket_1 = new_basket.copy()
new_basket_1.extend([12334,213])
print(basket)
print(new_basket)
print(new_basket_1)

#reversed()
rev_list = [1,2,3,4]
print(rev_list[::-1])
print(rev_list)
rev_list.reverse()
print(rev_list)

#range
print(list(range(1,101)))

#List Unpacking
a,b,c,*ot, d = [1,2,3,4,5,6,7]
print(a)
print(b)
print(c)
print(ot)
print(d)
