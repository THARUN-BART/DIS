import html

x = "<script>alert('XSS')</script>"

print("Unsafe:", x)

safe = html.escape(x)
print("Safe:", safe)