p, q = 13, 17
n = p*q
phi = (p-1)*(q-1)

e = 5
d = pow(e, -1, phi)

msg = 10
enc = pow(msg, e, n)
dec = pow(enc, d, n)

print("Encrypted:", enc)
print("Decrypted:", dec)