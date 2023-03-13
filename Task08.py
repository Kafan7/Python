# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек, которое будет в длине шоколадки: '))
m = int(input('Введите количество долек, которое будет в ширине шоколадки: '))
k = int(input('Введите количество долек, которые хотите отломить от данной шоколадки: '))

if k % n == 0 and k % m == 0:
    print(f'От шоколадки заданных размеров можно отломить {k} долек одним разломом по прямой')

else:
    print(f'От шоколадки заданных размеров невозможно отломить {k} долек одним разломом по прямой')