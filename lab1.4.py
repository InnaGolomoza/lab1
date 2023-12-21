"""Користувач вводить рядок, у якому чергуються цифри та інші символи.
На початку і у кінці рядка цифри відсутні. Напишіть програму, яка друкує усі
символи введеного рядка у тому ж порядку, але без цифр.
Голомоза Інна Андріївна"""

#Введення данних
s = input("Введіть рядок: ") 

result = s.replace("0","")
result = result.replace("1","")
result = result.replace("2","")
result = result.replace("3","")
result = result.replace("4","")
result = result.replace("5","")
result = result.replace("6","")
result = result.replace("7","")
result = result.replace("8","")
result = result.replace("9","")
   
#Виведення данних
print("Результат: ", result)
