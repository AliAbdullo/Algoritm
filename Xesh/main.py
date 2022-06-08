# Xeshni linear search bilan 
def linear_search(list, item): # Ro'yxat va qidirilayotgan element
    for n in range(len(list)): # Ro'yxat uzunligidagi sonlar to'plamini yaratib olamiz va istalgan birini tanlab oladi
        if list[n]==item: # Tanlangan indeks ostidagi qiymat bilan qidirilayotgan element solishtiriladi
            return n
    return None

# Xeshni binary search bilan 
def binary_search(list, item):  #
    low = 0                     #boshlanish qisimni aniqlab olamiz
    high = len(list)-1          #tugash nuqtasi
    while low <= high:          #Agar boshi oxirgi nuqtadan kichik bo'lsa loopimiz davom etadi
        mid = (low + high)//2   #
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



if __name__ == '__main__':
    myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
    print(linear_search(myList1,99))
    print(binary_search(myList1,56))
    
    myList2 = [18,12,25,1,3,4,10,5,23,4,13,89]
    myList2.sort()
    print(linear_search(myList2,13))
    print(binary_search(myList2,13))
    mevalar = ['olma','anor','olcha','behi','shaftoli','anjir']
    # mevalar.sort()
    print(mevalar)
    print(binary_search(mevalar,'behi'))