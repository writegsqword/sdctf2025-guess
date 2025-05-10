import os
import zipfile




zip_file = zipfile.ZipFile("guesses.zip", "w")

def write_file(fname, content):
    #with open(fname, "w") as f:
    #    f.write(content)
    zip_file.writestr(fname, content)
lim = 10000000
for i in range(0, lim, 1000):
    write_file(f"{i}.txt", str(i))


zip_file.close()
