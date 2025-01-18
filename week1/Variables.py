x = 5
print(type(x))
x = "John"
print(type(x))
#то есть типизация динамическая 

print("legal variable name can not be started from number, can not contain space ' ' and '-'")

#так же можно обьявить несколько переменных в одной строке
a, b, c = 5, "banana", True
print(a,b,c)


#глобальные переменные

y = 10
def myfunc():
  y = 9
  print("y = ", y)

myfunc()

print("y = ", y) 