##  Algoritm
## N factorialni xisoblash: N = 5 bo'sa, 5 factorial algoritmi:

#1.Start
#2.N va i o'zgarubchilarini yaratib olamiz.
#3.o'zgaruvchilarga qiymat joylymiz
#4.Faktarilga 1 qiymat beramiz va i ga ko'paytiramiz va qiymatni faktorialga joylaymiz:
# factorial = factorial * i
#5. i+=1 
#    
#   aks holda c katta 
#6.Natijani foydalanuvchiga qaytarish



def factorial(N):
    i=1
    fact=1
    while i!= N+1:
        fact = fact*i
        i +=1
    return fact
print(factorial(5))
