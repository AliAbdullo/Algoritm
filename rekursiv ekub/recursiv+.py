
def summa(array):
    if array==[]:
        return 0
    return array[0]+summa(array[1:])  
list=[5,4,8,63]
print(summa(list))