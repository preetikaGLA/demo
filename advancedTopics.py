#list comprehension in python
a=[x**2 for x in range(1,5)]
print(a)

#generator() function added
def gen():
  for x in range(5,11):
    yeald x**2
a=gen()
print('print generator object',a)
print('next value',next(a))
