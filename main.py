#1-misol
n = int(input())

if n > 0:
    print("Musbat")
elif n < 0:
    print("Manfiy")
else:
    print("0")

#2-misol
n = int(input())

if n % 3 == 0 and n % 4 == 0:
    print("3 ga ham, 4 ga ham bo‘linadi")
else:
    print("Bo‘linmaydi")

#3-misol
y = int(input())

if y <= 12:
    print("Bola")
elif y <= 18:
    print("O‘smir")
elif y <= 60:
    print("Katta")
else:
    print("Qariya")

#4-misol
a = int(input())
b = int(input())

if a > b:
    print("Katta:", a)
elif b > a:
    print("Katta:", b)
else:
    print("Teng")

#5-misol
t = int(input())

if t < 0:
    print("Juda sovuq")
elif t < 15:
    print("Sovuq")
elif t < 25:
    print("Yoqimli")
else:
    print("Issiq")
