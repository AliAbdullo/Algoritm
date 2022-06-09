from pprint import pprint as print


graph={
    'A':{'B':2, 'C':6},
    'B':{'C':3, 'D':4},
    'C':{'D':5, 'E':6},
    'D':{'F':5},
    'E':{'F':0},
    'F':{}
}
street = {
  'A':{'B':2, 'C':6},
  'B':{'C':3, 'D':4},
  'C':{'D':5, 'E':6},
  'D':{'F':5},
  'E':{'F':0},
  'F':{}
}
print(graph)
print(street)

narxlar = {
  'B':2,
  'C':6,
  'D': float('inf'),
  'E': float('inf'),
  'F': float('inf')
}

otalar = {
  'B':'A',
  'C':'A',
  'D': None,
  'E': None,
  'F': None,
}
process = []

def eng_arzon_tugun_top(narxlar):
    eng_arzon = float('inf')
    eng_arzon_tugun =None
    for tugun in narxlar:
        narx = narxlar[tugun]
        if narx < eng_arzon and tugun  not in process:
            eng_arzon = narx
            eng_arzon_tugun = tugun 
    return eng_arzon_tugun

print(narxlar)
tugun = eng_arzon_tugun_top(narxlar)
print(f"Eng arzon tugun: {tugun}")

tugun = eng_arzon_tugun_top(narxlar) # A nuqtaga eng arzon tugundan boshlaymiz
print(tugun)

while tugun is not None:
    qoshnilar = graph[tugun] # Eng yaqin tugunning qo'shnilarini topamiz
    narx = narxlar[tugun] # Ularning narxini olamiz
    for qoshni in qoshnilar.keys(): # Har bir qo'shni uchun...
        yangi_narx = narx + qoshnilar[qoshni] # shu qo'shniga borish narxini hisoblaymiz
        if narxlar[qoshni]>yangi_narx: # agar bu tugunga borish avvalgidan arzonroq bo'lsa:
            narxlar[qoshni] = yangi_narx # shu tugunga borish narxini yangilaymiz
            otalar[qoshni] = tugun # va bu tugun otasini ham yangilaymiz.
    process.append(tugun) # tugunn ishlov berilgan tugunlar qatoriga qo'shamiz
    tugun = eng_arzon_tugun_top(narxlar)  