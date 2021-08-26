# *args and **kwargs

def func(*args, **kw):
  ase = 0
  for k in kw.values():
    ase += k
  return sum(args) + ase
  
print(func(1,2,3,4, k1=1, k2=3))