text = "HELLO"
key = "KEY"

key = (key * 2)[:len(text)]

enc = ""
for t, k in zip(text, key):
    enc += chr((ord(t)-65 + ord(k)-65) % 26 + 65)

dec = ""
for e, k in zip(enc, key):
    dec += chr((ord(e)-65 - (ord(k)-65)) % 26 + 65)

print("Encrypted:", enc)
print("Decrypted:", dec)