from Crypto.Util.number import *
from Crypto import Random
import Crypto
import math
import time
import gmpy2
import sys
import random 

bits= int(input("Enter no. of bits "))
with open ("msgfile.txt", "r") as msgfile:
    msg=msgfile.readlines()

#print("Message = " + str(msg) + "\n\n")

start_key = time.time()
power_p = 1
power_q = 1
p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
#print("p = " + str(p))
for i in range(3):
    power_p = power_p*p
#print("powered p = "+str(power_p)+"\n\n")

q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
for i in range(1):
    power_q = power_q*q
#print("q = "+str(power_q)+"\n\n")

n = power_p*power_q
#print("n = "+str(n)+"\n\n")
if p == q:
    PHI = power_p*(p-1)
else:
    temp_p = power_p//p
    temp_q = power_q//q
    PHI=temp_p*(p-1)*temp_q*(q-1)
#print("PHI = "+str(PHI)+"\n\n")

e = 65537
d = (gmpy2.invert(e, PHI))
end_key = time.time()
print("Private Key Generation time in milliseconds : " + str((end_key - start_key)*1000))
#print("d = "+str(d)+"\n\n")

start_enc = time.time()
cry = []
for i in msg:
    cr = pow(ord(i),e,n)
    cry.append(cr)
#print("cipher text: ",cry)
end_enc = time.time()
print("Encryption Time in milliseconds: " + str((end_enc-start_enc)*1000))


start_dec = time.time()
pl=""
for i in cry:
    pn = pow(i,d, n)
    pl += chr(pn)
#print("plain text: ",pl)
end = time.time()
end_dec = time.time()
print("Decryption Time : " + str((end_dec-start_dec)*1000))
