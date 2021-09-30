'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  d=1
  divizori=0
  while d<=n:
    if n%d==0:
      divizori+=1
    d+=1
  if divizori==2:
    return True
  else:
    return False
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  produs_numere=1
  for numar in lst:
    produs_numere = produs_numere*numar
  return produs_numere


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x!=y:
      if x<y:
        y=y-x
      else:
        x=x-y
  return x

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  r=x%y
  x=y
  y=r
  while(r):
    x=y
    y=r
    r=x%y
  return x
def main():
  lista=[3, 4, 5]
  print(is_prime(22))
  print(get_cmmdc_v1(16,4))
  print(get_cmmdc_v2(25, 5))
  print(get_product(lista))

if __name__ == '__main__':
  main()
