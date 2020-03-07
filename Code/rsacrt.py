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
#p = 15703444645413011497
#p =  179527255883986189312370454583256338593009148521039016556393991794876031033684918857026604095163498007289709699865541376473302259865222240933627317246843512580472513205413143496297207422415629161514519024102597845194318443573060089236527271053292061267927855117953986431802873050144538729202386898443016950871
#print("p = "+str(p)+"\n\n")

q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
#q = 17568850307469666853
#q = 116568994255094452785941984694864003197976903002306696391867782066284075839324717309460113750947403547284268879511329435057524121475938405567769327244028564539814150488986123437632843926427446810662580236903702500449086733373280719828614051568008907411008987133259088311340437740822870672498306606649540870573
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
"""
start_enc = time.time()
cry = []
for i in msg:
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
#print("plain text : ",pl)
print("Decryption time in microseconds : " + str((end_dec-start_dec)*1000))
"""