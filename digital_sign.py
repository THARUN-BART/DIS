from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

key = rsa.generate_private_key(65537, 2048)
msg = b"Hello"
pad = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)

sig = key.sign(msg, pad, hashes.SHA256())

try:
    key.public_key().verify(sig, msg, pad, hashes.SHA256())
    print("VALID")
except Exception:
    print("INVALID")