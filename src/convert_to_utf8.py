raw = open('avengers.csv', 'rb').read()
decoded = raw.decode ('ISO-8859-1')
encoded = decoded.encode ('utf-8')
with open ('avengers_utf8.csv', 'w') as file:
    file.write(decoded)
