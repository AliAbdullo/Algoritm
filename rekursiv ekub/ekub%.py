# Yevklid algoritmi. Qoldiq usuli

def ekub(a,b):
  if a == 0:
    return b
  return ekub(b%a, a) 

print(ekub(9,3))