#Yevklid algoritmi. Qoldiq usuli

def ekub(a,b):
  if a == 0:
    return b
  if a>b:
     a,b=b,a
  return ekub(b-a,a)

print(ekub(9,6))