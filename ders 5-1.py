import random

if 5<3:
    print("if bloğuna gir")
elif 8>7:
    print("elif bloğuna girdi") # 2.İF
else:
    print("else bloğuna girdi")
#
#  
print("sorgulanacak sayıyı giriniz")
Sayi1=int(input())
if Sayi1%2==1:
    print("Sayınız tektir")
else:
    print("Sayınız çiftir")

print("lütfen karşılaştıracağınız sayıları giriniz")
Sayi2=int(input())
Sayi3=int(input())
if Sayi2>Sayi3:
    print("Girdiğiniz ilk sayi ikinci girdiğinizden büyüktür")
else:
    print("Girdiğiniz ilk sayi ikinci girdiğinizden küçüktür")
#
#
Sayi4=random.randint(1,100)
Sayi5=random.randint(1,100)

print("İlk Sayi:{} ve İkinci sayi:{}".format(Sayi4,Sayi5))

if Sayi4>Sayi5:
    print("İlk Sayi ikinciden büyük")
else:
    print("İlk Sayi ikinciden küçük")
    
#
#

