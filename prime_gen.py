import Crypto
from Crypto import Util
from Crypto.Util import number
prime_list = [] #list of all primes
answer_list = []
def prime_gen (bit):
  x = number.getPrime(int(bit))
  if x not in prime_list:  
    prime_list.append(x)
    return int(x)
  else:
    prime_gen(bit)
x = int(input("how many outputs"))
y = input("how many bits")
for i in  range (0, x , 1):
  if len (answer_list)%2 == 0:
     answer_list.append((prime_gen(y))*(prime_gen(y)))
  elif len (answer_list)%2 == 1:
    answer_list.append(prime_gen(y)*int(prime_list[0]))
print (answer_list)              
print (prime_list)