##  Algoritm
## Uchta sondan eng kattasini topish algoritmi:

#1.Start
#2.a,b va c o'zgarubchilarini yaratib olamiz.
#3.o'zgaruvchilarga qiymat joylymiz
#4.Agar a>b bo'lsa:
#   *a>c bo'lsa   a katta
#   aks holda:
#   c katta 
#5.Yoki b>a bo'lsa 
#   b>c bo'lsa  b katta 
#   aks holda c katta 
#6.Natijani foydalanuvchiga qaytarish
def katta(a,b,c):
  if a > b:
    if a > c:
      return f"Sonlar ichida kattasi: {a}"
    else:
      return f"Sonlar ichida kattasi: {c}"
  else:
    if b > a:
      if b > c:
        return f"Sonlar ichida kattasi:{b}"
      else:
        return f"Sonlar ichida kattasi:{c}"     
 #Tekshiramiz:
print(katta(6,65,45))