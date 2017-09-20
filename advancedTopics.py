#list comprehension in python
a=[x**2 for x in range(1,5)]
print(a)

#generator expression
b=(x**2 for x in range(5,11))
print('generator object',b)
print('next value',next(b))

#map()
a=map(lambda x:x**2,range(1,10))
print(a)
