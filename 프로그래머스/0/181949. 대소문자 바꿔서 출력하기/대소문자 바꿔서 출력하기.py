st = input()
for c in st:
    if c.isupper():
        print(c.lower(), end='')
    else:
        print(c.upper(),end='')
