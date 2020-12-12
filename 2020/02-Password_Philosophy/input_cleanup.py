import os

sed_cleanup = ["-", ": "]
for i in range(2):
    os.system("sed -i 's/" + sed_cleanup[i] + "/ /g' input")
