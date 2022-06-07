# Binary Search ro'yxatdan element qidirish
def BinarySearch(array,value,start=0,end=None):
# Yuqori chegarani tekshirib olamiz
    if end is None:
        end = len(array)-1  #Agar yuqori chegara  belgilanmagan bo'lsa arrayni uzunligini beramiz
    if start > end:  #Boshi va yuqori chegara solishtiriladi
        return None

    mit = (start + end )//2
    if array[mit] == value:
        return mit
    elif array[mit] > value:
        return BinarySearch(array,value,start,mit+1)
    else:
        return BinarySearch(array, value,mit-1,end)
    return None


array1=list(range(40))
print(BinarySearch(array1,15))