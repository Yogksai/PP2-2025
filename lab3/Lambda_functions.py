#lambda function
x = lambda a : a + 10
print(x(5)) 

#anu number of arguments
x = lambda a, b : a * b
print(x(5, 6)) 

#
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))