#Quick sort yordamida royxatni tartiblash
from random import randrange
def qsort(array):
    """Ro'yxatni tartiblash"""
    if len(array)<2:
        return array
    else:
      pivot = array.pop(randrange(len(array)))
      kichik = [i for i in array if i <= pivot]
      katta = [i for i in array if i >pivot ]
      print(f"{kichik} + [{pivot}] +{katta}")
      return qsort(kichik) + [pivot] + qsort(katta)
                        

array3 = list(range(20))
lit =[344,34,4,8,5,9,3,1,0,14,7,2,34]
print(array3,lit)
print(qsort(lit))
print(qsort(array3))