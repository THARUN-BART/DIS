from Crypto.Cipher import DES, AES

# DES (8-byte key, 8-byte block)
des_key, des_msg = b"12345678", b"8ByteMsg"
des_enc = DES.new(des_key, DES.MODE_ECB).encrypt(des_msg)
des_dec = DES.new(des_key, DES.MODE_ECB).decrypt(des_enc)
print("DES:", des_enc, des_dec)

# AES (32-byte key for AES-256, 16-byte block)
aes_key, aes_msg = b"12345678901234567890123456789012", b"16ByteMessage!!"
aes_enc = AES.new(aes_key, AES.MODE_ECB).encrypt(aes_msg)
aes_dec = AES.new(aes_key, AES.MODE_ECB).decrypt(aes_enc)
print("AES:", aes_enc, aes_dec)