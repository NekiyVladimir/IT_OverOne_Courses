a) a = int(input())
if int(a)%1000==0:
    print('millennium')
else:
    print('не делится без остатка')
b) a = int(input())
if a>=0 and a<20:
    print('home')
elif a>=20 and a<=50:
    print('cafe')
elif a>50:
    print('restourant')
else:
    print('error')
c) a = str(input())
if len(a)>=10:
    print(input(),'!!!')
elif len(a)<10:
    print(a[1])
else:
    print('error')

d) a = input()
b=int(len(a)/2)
if a[b] == a[0]:
    print(a[0:b+1])
else:
    print(a[b])
