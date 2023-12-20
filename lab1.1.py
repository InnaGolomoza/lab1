"""Оленка дізналася, що їй для сну треба t хвилин. На відміну від Тетяни,
Оленка лягає спати після опівночі в h годин і m хвилин.Допоможіть Оленці
визначити, на який час їй поставити будильник, щоб він продзвенів рівно
через t хвилин після того, як вона ляже спати. В окремих рядках вводяться
значення t, h і m відповідно. Гарантується, що Оленка повинна прокинутися
в той же день, що і заснути. Програма повинна виводити час, на який потрібно
поставити будильник: в першому рядку години, в другому - хвилини.
Голомоза Інна Андріївна"""


#Введення даних
t = int(input("Введіть скільки хвилин ви хочете спати: "))
h = int(input("Введіть годину, коли ви лягаєте спати: "))
m = int(input("Введіть хвилини, коли ви лягаєте спати: "))

hour = (h + (m + t) // 60) % 24
minute = (m + t) % 60

#виведення результату
print("Поставте будильник на {}:{}".format(hour, minute ))

