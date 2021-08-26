# Scope - what variables do I have access to?

total = 0
def count():
  global total
  total += 1
  return total

count()
count()
print(count())

def count1(total):
  return total + 1

total1 = 0
print(count1(count1(count1(total1))))
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions