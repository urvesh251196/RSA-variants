from Crypto.Util.number import *
from Crypto import Random
import Crypto
import time
import gmpy2
import sys

bits= int(input("Enter no. of bits "))
with open ("msgfile.txt", "r") as msgfile:
    msg=msgfile.readlines()

#print("Message = " + str(msg) + "\n\n")

#no_of_primes = input("Enter no. of primes : ")
no_of_primes = 3
start_key = time.process_time()
primes = []

for i in range(int(no_of_primes)):
    primes.append(Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes))
    #print("prime "+ str(i+1) +" = " + str(primes[i])+"\n\n")

n = 1
for i in range(int(no_of_primes)):
    n *= primes[i]
#print("n = "+str(n)+"\n\n")

PHI = 1
for i in range(int(no_of_primes)):
    PHI *= primes[i] - 1

#PHI=(p-1)*(q-1)*(r-1)
#print("PHI = "+str(PHI)+"\n\n")

e = 65537

d = (gmpy2.invert(e, PHI))
end_key = time.process_time()
#print("d = "+str(d)+"\n\n")
print("Key Generation in milliseconds : " + str((end_key - start_key)*1000))

start_enc = time.time()
cry = []
for temp in msg:
    for i in temp:
        cr = pow(ord(i),e,n)
        cry.append(cr)
end_enc = time.time()
#print("cipher text: ",cry)
print("Encryption in milliseconds : " + str((end_enc - start_enc)*1000))

start_dec = time.time()
pl=""
for i in cry:
    pn = pow(i,d,n)
    pl += chr(pn)
print("plain text: ",pl)
end_dec = time.time()
print("Decryption in milliseconds : " + str((end_dec - start_dec)*1000))