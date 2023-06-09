# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

print("Проверка билета, счастливый он или нет?")
number_of_ticket = input("Введите номер билета: ")

if len(number_of_ticket) == 6:
    if int(number_of_ticket[0]) + int(number_of_ticket[1]) + int(number_of_ticket[2]) == int(number_of_ticket[3]) + int(number_of_ticket[4]) + int(number_of_ticket[5]):
        print("Да! Это счастливый билет!:)")
    else:
        print("К сожалению, это не счастливый билет!:(")
else:
    print("Упс! Чтобы определить, счастливый билет или нет, нужен такой билет, у которого шестизначный номер. Где сумма первых трёх цифр равна сумме последних трёх.")
