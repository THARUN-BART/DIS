from pycipher import Playfair

pf = Playfair("KEYWORDABCDEFGHILMNPQSTUVXZ")

enc = pf.encipher("HELXLO")
dec = pf.decipher(enc)

print("Encrypted:", enc)
print("Decrypted:", dec)