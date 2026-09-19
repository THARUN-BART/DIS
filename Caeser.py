text = "HELLO"
key = 3

enc = ""
for c in text:
    enc += chr((ord(c)-65+key)%26+65)

dec = ""
for c in enc:
    dec += chr((ord(c)-65-key)%26+65)

print("Encrypted:", enc)
print("Decrypted:", dec)