# Bubble Sort algoritmi.
def bubbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                 print(f"{array[j]}, {[array[j+1]]}")
                 array[j],array[j+1]=array[j+1],array[j]


array3 = list(range(39))
array1=list(range(40))
array0 = [5,9,6,3,7,1,0,6]
print(bubbleSort(array0))