# Quick yordamida ro'yxatni tartiblash
from random import randrange
def qsort(list): #Quick sort funksiyasini xosil qilib ro'yxat qabul qiladigan qilamiz
    if len(list) < 2:   #Ro'yxatda element bor yoki yo'qligini tekshirib olamiz
        return list
    else:
        pivot = list.pop(randrange(len(list)))
        kichik = [i for i in list if i < pivot]
        katta = [ i for i in list if i > pivot]
        print(f"{kichik} + [{pivot}] + {katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

list1 = [2,7,4,5,8,6,9,7,13,0,1,365,4,10,65,978,41,3,65,84,5145,12,41]      
list2 = list(range(20)) 
print(list1)

print(qsort(list1))  
print(list2)
print(qsort(list2))