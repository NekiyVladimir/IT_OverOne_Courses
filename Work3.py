a) while True:
    X = int(input())
    Y = int(input())
    sign = str(input())
    Z = 0
    if sign == '+':
        print('Z =', X+Y)
    elif sign == '-':
        print('Z =', X-Y)
    elif sign == '*':
        print('Z =', X*Y)
    elif sign == '/':
       print('Z =', X/Y)
    elif sign == '/' and Y == 0:
        print('error')
    elif sign == '0':
        break
    else:
        print('error')
print(Z)

b) a = int(input())
summ = 0
proizv = 1
while a != 0:
    proizv = proizv *(a%10)
    summ += a%10
    a =a//10
print('Сумма =',summ)
print('Произведение =', proizv)

number=''
while not number.isdigit():
    number = input()
summ = 0
mul = 1
for i in number:
    summ += int(i)
    mul *= int(i)

c) for n in range(200, 300):
    s = 0
    for i in range(1,n):
        if n%i == 0:
            s+=i
    if s>n:
        result = 0
        for i in range(1, s):
            if s%i == 0:
                result+=i
        if result == n:
            print(n, s)

sum_result = []
for n in range(200, 301):
    result = []
    i = 1
    # i - делитель, n - число
    while i<n:
        if n%i == 0:
            divider = n/i
            result.append(divider)
            i+=1
    else:
        i+1
    sum_result.append(sum(result))
for i in range(1,101):
    for g in range(1,101):
        if sum_result[i] == 200+g and sum_result[g] == 200+i:
            print(f'{200+i}-{200+g}')

d) n=int(input())
summ = 0
for i in range(1, n+1):
    summ+= 1/i
print(summ)

e)a = [23, 54, 21, 23, 42, 78, 32, 97, 46, 85, 77, 88, 90, 98, 99, 44, 45, 47, 65]
n = max(a)
m=len(a)
for i in range(m):
    if a[i]%2 == 0:
        a[i]=n
print(n)
print(a)

f) a = [23, 54, 21, 23, 42, 78, 32, 97, 46, 85, 77, 88, 90, 98, 99, 44, 45, 47, 65]
counter  = 0
numb = a[0]
n = len(a)
for i, number in enumerate(a):
    if numb < number:
        numb = number
    else:
        numb = number
        if numb<a[i+1] and i+1<n:
            counter+=1
print(counter)

g) a = [[1,7,9],
     [4,2,7],
     [9,2,6]]
n=len(a)
for i in range(n):
    max_n = a[i][0]
    temp_g = 0
    #  temp_g - индекс по столбцу
    for g in range(n):
        if max_n<a[i][g]:
            max_n = a[i][g]
            temp_g=g
    a[i][i], a[i][temp_g]=a[i][temp_g], a[i][i]
    # замена элементов в матрице
print(a)

h) string = input()
str_lst = string.split(' ')
result = ' '.join(reversed(str_lst))
# join - соединяет элементы списка в строку, reserved - переворачивает строку
print(result)
