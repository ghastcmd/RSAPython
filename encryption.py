import math
import random as rnd

# returns a more above approximation of sqrt
def sqrtop(n):
  i = 2
  while True:
    if (i - 1)**2 <= n and i**2 >= n:
      return i
    i += 1
  return 0

# executes the extended euclidean algorithm
def EEA(a: int, b: int, x: list, y: list):
  if a == 1:
    x[0] = 1
    y[0] = 0
    return

  x1 = [0]
  y1 = [0]
  EEA(b % a, a, x1, y1)
  x[0] = y1[0] - (b // a) * x1[0]
  y[0] = x1[0]

# returns the coeficient that solves the inverse
# mod function (a * d mod b = 1)
def inv_mod(a, b):
  x = [0]
  y = [0]
  EEA(a, b, x, y)
  return (x[0] + b) % b

# returns if a number is prime or not
def is_prime(a):
  for b in range(2, sqrtop(a)):
    if a % b == 0:
      return False
  return True

#returns the next prime of a number
def next_prime(a):
  a += 1
  while is_prime(a) == False:
    a += 1
  return a

# calculates the lowest common multiplier of 2 numbers
def lcm(a, b, p = 2):
  mod_a = a % p
  mod_b = b % p
  if mod_a == 0:
    a = a // p
  if mod_b == 0:
    b = b // p

  if a == 1 and b == 1:
    return p
  else:
    if mod_a == 0 or mod_b == 0:
      return lcm(a, b, p) * p
    else:
      return lcm(a, b, next_prime(p))

# return the euler totient function
# it must not return a value with factor of e
def get_phi(p, q, e):
  phi = (p - 1) * (q - 1)
  if phi % e == 0:
    print('valor de e é inválido para os valores de p e q')
    return False
  return phi


# returns the lambda (lcm(p-1, q-1))
def phi_lambda(p, q):
  return lcm(p - 1, q - 1)

# get p and q which are prime numbers
def get_prime():
  b = rnd.randint(10**10, 10**11)
  return next_prime(b)

# RSA cryptography function
def crypt_rsa(a, e, n):
  return (a**e) % n

# RSA decryptography function
def decrypt_rsa(a, d, n):
  return (a**d) % n

# parses string of numbers to list of int
def parse_int(any_str):
  val = 0
  numbers = []
  for an in any_str:
    if an >= '0' and an <= '9':
      val = val * 10 + ord(an) - ord('0')
    if an == ' ':
      numbers.append(val)
      val = 0
  numbers.append(val)
  return numbers

# encrypt string
def string_enc(char, e, n):
  numbers = []
  for i in char:
    if i == ' ':
      ltr = 28
    else:
      ltr = ord(i) - ord('A') + 2
    
    numbers.append(crypt_rsa(ltr, e, n))
  return numbers


# decrypt string
def string_dec(char, d, n):
  nums = []
  nums = parse_int(char)
  letters = []
  for an in nums:
    ltr = decrypt_rsa(an, d, n)
    if ltr == 28:
      letters.append(' ')
    else:
      letters.append(chr(ltr + ord('A') - 2))
  return letters

# returns the decryption key(generates it)
def get_dec(p, q, e):
  phi = (p-1)*(q-1)
  return inv_mod(e, phi)

# main calls
# Testing the implementation
'''
p = 61
q = 53
e = 17

n = p * q
d = get_dec(p, q, e)

print(d, n)

lets = string_enc('ALELO VOADOR', e, n)
print(lets)
dec = string_dec(str(lets), d, n)
dec = ''.join(dec)
print(dec)

alelo = lcm(7, 3)
print('>>>>',alelo)

p = 61
q = 53
e = 17

#p = int(input('insira p primo: '))
#q = int(input('insira q primo: '))
#e = int(input('insira valor de e: '))


phi = phi_lambda(p, q)
d = inv_mod(e, phi)
n = p * q

char = input('Insira mensagem a ser criptografada: \n')

string_enc(char, e, n)

string = '1752 47 824 47 134 1075 2037 134 1752 3086 134 615 1075 1387 134 2549 1075 134 47 134 2369 134 1188 824 3023'

string_dec(string, d, n)
#string_dec(char, d, n)

#print('phi>', phi, ' n>', n, ' d>', d)

#input('Press enter to exit... ')
'''