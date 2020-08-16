name=input( "Как тебя зовут?" )
age=input( "Сколько тебе лет?" )

print( " Привет " + name + "!" )
print( " Тебе " + str(age) + " лет " + "!" )


from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.GREEN )
print( Fore.BLACK )

what=input("Что делаем? (+,-)")

print( Back.CYAN )

a=float(input("Введите первое число:"))
b=float(input("Введите второе число:"))

print( Back.YELLOW )

if what=="+":
    c=a+b
    print("Результат:" + str(c))
elif what== "-":
    c=a-b
    print("Результат" + str(c))
else:
    print("Выбрана неверная операция")

input()
