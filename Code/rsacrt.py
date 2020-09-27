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

start_pkey = time.process_time()
p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
#print("p = "+str(p)+"\n\n")

q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
#print("q = "+str(q)+"\n\n")

n = p*q
#print("n = "+str(n)+"\n\n")

PHI= (p-1)*(q-1)
#print("PHI = "+str(PHI)+"\n\n")

e = 65537
 
d = (gmpy2.invert(e, PHI))
dp = d%(p-1)
dq = d%(q-1)
qinv = (gmpy2.invert(q,p))



#print("d = "+str(d)+"\n\n")
end_pkey = time.process_time()

print("Key Generation time in microseconds : " + str((end_pkey-start_pkey)*1000))

start_enc = time.time()
cry = []
for temp in msg:
    for i in temp:
        cr = pow(ord(i),e,n)
        cry.append(cr)
    
end_enc = time.time()
#print("cipher text: ",cry)
print("Encryption time in microseconds : " + str((end_enc-start_enc) *1000))

start_dec = time.time()
pl = ""
for i in cry:
    pn1 = pow(i,dp,p)
    pn2 = pow(i,dq,q)
    h = (qinv*(pn1-pn2))%p
    pl += chr(pn2 + h*q)
end_dec = time.time()
print("plain text : ",pl)
print("Decryption time in microseconds : " + str((end_dec-start_dec)*1000))
