import hashlib

text = "hello world"

print("MD5:", hashlib.md5(text.encode()).hexdigest())
print("SHA:", hashlib.sha256(text.encode()).hexdigest())