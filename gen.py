import os
import zipfile
import sys

try:
    os.remove('guesses.zip')
except:
    pass
zip_file = zipfile.ZipFile("guesses.zip", "w")

def write_file(fname, content):
    #with open(fname, "w") as f:
    #    f.write(content)
    zip_file.writestr(fname, content)

chunk = int(sys.argv[1])
lim = 125000000 * 2
#ideal step size is 1136 but i dont want to deal with round errors
for i in range(lim * chunk, lim * (chunk + 1), 2000):
    write_file(f"{i}.txt", str(i))


zip_file.close()
