import os
import zipfile




zip_file = zipfile.ZipFile("guesses.zip", "w")

def write_file(fname, content):
    #with open(fname, "w") as f:
    #    f.write(content)
    zip_file.writestr(fname, content)
lim = 500000000
#ideal step size is 1136 but i dont want to deal with round errors
for i in range(-lim, lim, 2000):
    write_file(f"{i}.txt", str(i))


zip_file.close()
