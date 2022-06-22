import random
def Fermat(a, x, n):
  if x == 0:
    return 1;
  elif x%2 == 0:
    t = Fermat(a, x/2, n);
    return (t*t)%n;
  else:
    t = Fermat(a, x-1, n);
    c = a%n;
    return (t*c)%n;

def Es_Compuesto(a, n, t, x):
  x0 = Fermat(a, x, n)
  if x0 == 1 or x0 == n-1:
    return False;
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
  while Miller(n,23) == False:
    n = n+2
  return n

def EUCLIDES(a, b):
  if b == 0:
    return a;
  else:
    return EUCLIDES(b, a%b)

def EUCLIDES_EXT(a, b):
    if b == 0:
        return 0,1,0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
 
    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        a = b
        b = r
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
    return u0
def INVERSO(a, n):
    if EUCLIDES(a,n) == 1:
      return EUCLIDES_EXT(a,n)%n
    else:
      return 0
def RSA_KEY_GENERATOR(k):
  p = Randomgen(k//2)
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


count = 1
ed = RSA_KEY_GENERATOR(63)
palabra = random.randint(1,99)
c = Cifrado(palabra, ed[1],ed[0])
m = Descifrado(c, ed[2],ed[0])
while(count < 10):
  ed = RSA_KEY_GENERATOR(64)
  c = Cifrado(palabra, ed[1],ed[0])
  m = Descifrado(c, ed[2],ed[0])
  if(m == palabra):
    print(palabra)
    print(ed)
    print(c)
    print(m)
    palabra = random.randint(1,99)
    count += 1
