from Crypto.Util.number import *
#from Crypto import Random
import Crypto
import time
import gmpy2
import sys

bits= 256
msg="Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]Large-print (also large-type or large-font) refers to the formatting of a book or other text document in which the typeface (or font), and sometimes the medium, are considerably larger than usual, to accommodate people who have poor vision. Often public special-needs libraries will stock large-print versions of books, along with versions written in Braille.  The standard font size for large print is at least 18 points in size, but different sizes are made to suit different visual needs.[1]"
#print("Message = " + str(msg) + "\n\n")
start_key = time.time()
p = getRandomNumber(bits, randfunc=None)
print("p = "+str(p)+"\n\n")

q = getRandomNumber(bits, randfunc=None)
print("q = "+str(q)+"\n\n")

n = p*q
#print("n = "+str(n)+"\n\n")

PHI=(p-1)*(q-1)
#print("PHI = "+str(PHI)+"\n\n")

e = 65537

d = (gmpy2.invert(e, PHI))
end_key = time.time() 
#print("d = "+str(d)+"\n\n")
print("Key Generation in microseconds : " + str((end_key - start_key)*1000))
"""
start_enc = time.time()
cry = []
for i in msg:
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
#print("plain text: ",pl)
end_dec = time.time()
print("Encryption in microseconds : " + str((end_dec - start_dec)*1000))
"""