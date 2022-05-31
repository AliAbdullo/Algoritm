##  Algoritm misol:
##  1.Foydalanuvchi kiritgan ikki sonni yig'indisini qaytarish:
#1.Start 
#2.num1, num2 va summa degan o'zgaruvchilar yaratamiz.
#3.num1 va num2 ga qiymatlar yuklaymiz.
#4.num1 ni num2 ga qo'shamiz va yig'indini summa ga yuklaymiz:
#    num1 + num2 = summa
#5.Summani foydalanuvchiga qaytarish
#6.Stop

# a-variant
num1 = 9
num2 = 8
summa = 0
summa = num1 + num2
print(summa)
# b-variant: Function 
def xisob(son1,son2):
  natija = son1 + son2
  return natija

#  Tekshiramiz:
print(xisob(7,3))