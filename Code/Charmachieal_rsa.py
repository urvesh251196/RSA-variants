from Crypto.Util.number import *
from Crypto import Random
import Crypto
import time
import gmpy2
import sys
import math

bits= int(input("Enter no. of bits "))
with open ("msgfile.txt", "r") as msgfile:
    msg=msgfile.readlines()

#print("Message = " + str(msg) + "\n\n")
start_key = time.time()
p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
#print("p = "+str(p)+"\n\n")

q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
#print("q = "+str(q)+"\n\n")

n = p*q
#print("n = "+str(n)+"\n\n")

PHI=(p-1)*(q-1)

GCD = math.gcd(p-1,q-1)

    
PHI = PHI//GCD
#print("PHI = "+str(PHI)+"\n\n")

e = 65537

d = (gmpy2.invert(e, PHI))
end_key = time.time() 
#print("d = "+str(d)+"\n\n")
print("Key Generation in microseconds : " + str((end_key - start_key)*1000))

start_enc = time.time()
cry = []
for temp in msg:
    for i in temp:
        cr = pow(ord(i),e,n)
        cry.append(cr)
end_enc = time.time()
#print("cipher text: ",cry)
print("Encryption in microseconds : " + str((end_enc - start_enc)*1000))

start_dec = time.time()
pl=""
for i in cry:
    pn = pow(i,d,n)
    pl += chr(pn)
print("plain text: ",pl)
end_dec = time.time()
print("Decryption in microseconds : " + str((end_dec - start_dec)*1000))
