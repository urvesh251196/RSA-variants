import random
import time
import math
'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

'''
Tests to see if a number is prime.
'''
def generate_keypair(p, q):

    n = p * q
	

    #Phi is the totient of n
    phi = (p-1) * (q-1)
	
    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(pow(ord(char),key,n)) for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((pow(char,key,n))) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(pow(num,0.5))+2, 2):
        if num % n == 0:
            return False
    return True

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print "RSA Encrypter/ Decrypter"
    
    start = time.time()
    p=0
    q=0	
    while True:
        g=0
	a=0
	b=0	    
	g =  random.randrange(1, 1024)
    a =  random.randrange(1, math.floor(1024))
 	b =  random.randrange(1, math.floor(1024))

	p=2*g*a + 1
	q=2*g*b + 1
	h=2*g*a*b+a+b
	if is_prime(g) and gcd(a,b)==1 and is_prime(p) and is_prime(q) and is_prime(h):
	    break
            
    
     
    print "\nP=",p,"\nq=",q,"\ng=",g,"\na=",a,"\nb=",b,"\nh=",h,"\n"
    print "Generating your public/private keypairs now . . ."
    
    public, private = generate_keypair(p, q)
    End = time.time()
    print "Time For Generating Keys",(End-start)
    print "Your public key is ", public ," and your private key is ", private
    message = raw_input("Enter a message to encrypt with your private key: ")
    start = time.time()
    encrypted_msg = encrypt(private, message)
    End = time.time()
    print "Time For Encrypting",(End-start)
    print "Your encrypted message is: "
    print ''.join(map(lambda x: str(x), encrypted_msg))
    print "Decrypting message with public key ", public ," . . ."
    print "Your message is:"
    start = time.time()
    print decrypt(public, encrypted_msg)
    End = time.time()
    print "Time For Decrypting",(End-start)
