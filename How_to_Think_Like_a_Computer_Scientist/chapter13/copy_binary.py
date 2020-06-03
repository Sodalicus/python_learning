f = open("lorem.txt.gz", "rb")
g = open("loremcopy", "wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
         break
    g.write(buf)

f.close()
g.close()
