1)-5), 7) from random import randint
a = []
n = int(input())
summ = 0
summofrade = 0
for i in range(n):
    a.append([])
    for g in range(n):
        a[i].append(randint(1,15))
for i in a:
    print(i)
a_maxi = a[0][0]
a_mini = a[0][0]
for i in range(n):
    for g in range(n):
        if a_maxi <= a[i][g]:
            a_maxi = a[i][g]
        if a_mini>=a[i][g]:
            a_mini = a[i][g]
        summ += a[i][g]
for m in range(n):
    if sum(a[0])<=sum(a[m]):
        summofrade = a[m]
        ind = m
9) from random import randint
a = []
n = int(input())
for i in range(n):
    a.append([])
    for g in range(n):
        a[i].append(randint(1,15))

for i in a:
    print(i)

for i in range(n):
    for g in range(n):
        if i < g:
            a[i][g] = 0
        else:
            continue
for i in a:
    print(i)
10) from random import randint
a = []
n = int(input())
for i in range(n):
    a.append([])
    for g in range(n):
        a[i].append(randint(1,15))
for i in a:
    print(i)

for i in range(n):
    for g in range(n):
        if i > g:
            a[i][g] = 0
        else:
            continue
for i in a:
    print(i)

for l in range(n):
    if sum(a[0])>=sum(a[l]):
        summofrade = a[l]
        indl = l

print(f'Максимальное значение матрицы = {a_maxi}')
print(f'Минимальное значение матрицы = {a_mini}')
print(f'Сумма элементов матрцы = {summ}')
print(f'Индекс ряда с минимальной суммой элементов = {indl}')
print(f'Индекс ряда с максимальной суммой элементов = {ind}')

11) from random import randint
matrix_a = []
matrix_b = []
n = int(input())
for i in range(n):
    matrix_a.append([])
    for g in range(n):
        matrix_a[i].append(randint(1,15))
for l in range(n):
    matrix_b.append([])
    for m in range(n):
      matrix_b[l].append(randint(1,15))
for i in matrix_a:
    print(i)
for l in matrix_b:
    print(l)
c_matrix = []
ind_a = matrix_a[0][0]
ind_b = matrix_b[0][0]
for x in range(n):
    c_matrix.append([])
    for y in range(n):
        c_matrix[x].append(ind_a+ind_b)
        
for x in c_matrix:
    print(x)


1) a = int(input())
b = 0
def duim_santi(a):
    b = 2.54*a
    return(b)
print(duim_santi(a))
2) a = int(input())
b = 0
def santi_duim(a):
    b = a/2.54
    return(b)
print(santi_duim(a))
3) a = int(input())
b = 0
def mil_km(a):
    b = a*1.61
    return(b)
print(mil_km(a))
4) a = int(input())
b = 0
def km_mil(a):
    b = a/1.61
    return(b)
print(km_mil(a))
5) a = int(input())
b = 0
def funt_kg(a):
    b = a*0.454
    return(b)
print(funt_kg(a))
6) a = int(input())
b = 0
def kg_funt(a):
    b = a/0.454
    return(b)
print(kg_funt(a))
7) a = int(input())
b = 0
def gr_ync(a):
    b = a/28.35
    return(b)
print(gr_ync(a))
8) a = int(input())
b = 0
def ync_gr(a):
    b = a*28.35
    return(b)
print(ync_gr(a))
9) a = int(input())
b = 0
def gallon_litr(a):
    b = a*4.55
    return(b)
print(gallon_litr(a))
10) a = int(input())
b = 0
def litr_gallon(a):
    b = a/4.55
    return(b)
print(litr_gallon(a))
11)  a = int(input())
b = 0
def pinta_litr(a):
    b = a*0.568
    return(b)
print(pinta_litr(a))
12)  a = int(input())
b = 0
def litr_pinta(a):
    b = a/0.568
    return(b)
print(litr_pinta(a))


13) l =['1. Дюймы в сантиметры',
      '2. Сантиметры в дюймы',
      '3. Мили в километры',
      '4. Километры в мили',
      '5. Фунты в килограммы',
      '6. Килограммы в фунты',
      '7. Граммы в унции',
      '8. Унции в граммы',
      '9. Галлоны в литры',
      '10. Литры в галлоны',
      '11. Пинты в литры',
      '12. Литры в пинты']
for k in l:
    print(k)
a = int()
b = 0
def duim_santi(a):
    b = 2.54*a
    return(b)
def santi_duim(a):
    b = a/2.54
    return(b)
def mil_km(a):
    b = a*1.61
    return(b)
def km_mil(a):
    b = a/1.61
    return(b)
def funt_kg(a):
    b = a*0.454
    return(b)
def kg_funt(a):
    b = a/0.454
    return(b)
def gr_ync(a):
    b = a/28.35
    return(b)
def ync_gr(a):
    b = a*28.35
    return(b)
def gallon_litr(a):
    b = a*4.55
    return(b)
def litr_gallon(a):
    b = a/4.55
    return(b)
def pinta_litr(a):
    b = a*0.568
    return(b)
def litr_pinta(a):
    b = a/0.568
    return(b)
while True:
    n = int(input('Введите цифру, под которой находится нужный Вам перевод:'))
    if n == 1:
        a = int(input())
        duim_santi
        print(duim_santi(a))
    if n == 2:
        a = int(input())
        santi_duim
        print(santi_duim(a))
    if n == 3:
        a = int(input())
        mil_km
        print(mil_km(a))
    if n == 4:
        a = int(input())
        km_mil
        print(km_mil(a))
    if n == 5:
        a = int(input())
        funt_kg
        print(funt_kg(a))
    if n == 6:
        a = int(input())
        kg_funt
        print(kg_funt(a))
    if n == 7:
        a = int(input())
        gr_ync
        print(gr_ync(a))
    if n == 8:
        a = int(input())
        ync_gr
        print(ync_gr(a))
    if n == 9:
        a = int(input())
        gallon_litr
        print(gallon_litr(a))
    if n == 10:
        a = int(input())
        litr_gallon
        print(litr_gallon(a))
    if n == 11:
        a = int(input())
        pinta_litr
        print(pinta_litr(a))
    if n == 12:
        a = int(input())
        litr_pinta
        print(litr_pinta(a))
    if n>=13 or n<0:
        print('error')
    if n == 0:
        break
