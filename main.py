from email import message
from pydoc import describe
import random
def Fermat(a, x, n):
  if x == 0:
    return 1
  elif x%2 == 0:
    t = Fermat(a, x/2, n)
    return (t*t)%n
  else:
    t = Fermat(a, x-1, n)
    c = a%n
    return (t*c)%n

def Es_Compuesto(a, n, t, x):
  x0 = Fermat(a, x, n)
  if x0 == 1 or x0 == n-1:
    return False
  for i in range(t):
    x0 = Fermat(x0, 2, n)
    if x0==n-1:
      return False
  return True

def Miller(n,s):
  t = 0
  u = n-1
  while u%2==0:
    u = u/2
    t = t+1
  for j in range(s):
    a = random.randint(2,n-1)
    if Es_Compuesto(a,n,t,u):
      return False
  return True

def Randombits(b):
  po = 2**b
  pos = 2**(b-1)
  n = random.randint(0,po-1)
  m = pos + 1
  n = n | m
  return n

def Randomgen(b):
  n = Randombits(b)
  while Miller(n,136) == False:
    n = n+2
  return n

def EUCLIDES(a, b):
  if b == 0:
    return a
  else:
    return EUCLIDES(b, a%b)

def EUCLIDES_EXT(a,b):
 r = [a,b]
 s = [1,0] 
 t = [0,1]
 i = 1 
 q = [[]]
 while (r[i] != 0): 
  q = q + [r[i-1] // r[i]]
  r = r + [r[i-1] % r[i]]
  s = s + [s[i-1] - q[i]*s[i]]
  t = t + [t[i-1] - q[i]*t[i]]
  i = i+1
 return s[i-1]
def INVERSO(a, n):
    if EUCLIDES(a,n) == 1:
      return EUCLIDES_EXT(a,n)%n
    else:
      return 0
def RSA_KEY_GENERATOR(k):
  p = Randomgen(k//2)
  q = Randomgen(k//2)
  while(p == q):
    q = Randomgen(k//2)
  n = p*q
  _n = (p-1)*(q-1)
  for e in range(2,n):
    if EUCLIDES(e,_n) == 1:
      break
  d = INVERSO(e,_n)
  return [n,e,d]

def Cifrado(m,e,n):
  P = Fermat(m,e,n)
  return P

def Descifrado(c,d,n):
  S = Fermat(c,d,n)
  return S


cont = 1
valor = 64
mees = []
cif = []
inv = []
ed = RSA_KEY_GENERATOR(valor)
palabra = 33
c = Cifrado(palabra, ed[1],ed[0])
m = Descifrado(c, ed[2],ed[0])

while(m != palabra):
  ed = RSA_KEY_GENERATOR(valor)
  c = Cifrado(palabra, ed[1],ed[0])
  m = Descifrado(c, ed[2],ed[0])
n = ed[0]
e = ed[1]
d = ed[2]
print ("n =", n)
print ("e =", e)
print ("d =", d)
palabra = random.randint(0, 100)
while (cont <= 10):
  mees.append(palabra)
  
  c = Cifrado(palabra, e, n)
  cif.append(c)
  m = Descifrado(c, d, n)
  inv.append(m)
  palabra = random.randint(0, 100)
  cont +=1

print ()
print ("----------------------------------------------------------")
print ('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format("Mensaje", "|", "Cifrado","|", "Descifrado"))
print ("----------------------------------------------------------")
for i in range (len (mees)):
  print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(mees[i], "|", cif[i],"|", inv[i]))
  print ("----------------------------------------------------------")

