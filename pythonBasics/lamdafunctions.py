def multiply_by2(li):
  new_list = []
  for i in li:
    new_list.append(i*2)
  return new_list

print(multiply_by2([1,2,3]))

#map, filter, zip and reduce

#Map
def map_multipy(li):
  return li*2
print(list(map(map_multipy, [1,2,3])))

#Filter
def get_even(li):
  return li % 2 == 0
print(list(filter(get_even,[1,2,3,4,5])))

#Zip
print(list(zip([1,2,3],[6,7,8])))

#reduce
from functools import reduce

def accum(acc, i):
  print(acc, i)
  return acc + i

print(reduce(accum,[1,2,3],0))
