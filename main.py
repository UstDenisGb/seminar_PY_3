# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите N: '))
m = int(input('Введите M: '))
k = int(input('Введите K: '))

if k < m*n and (k%m==0 or k%n==0):
    print('МОЖНО')
else:
    print('НЕЛЬЗЯ')