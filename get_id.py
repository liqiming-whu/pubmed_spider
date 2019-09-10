import os


path = "d:/Eutils/geop/"

idlist = []
for filename in os.listdir(path):
    idlist.append(filename[:-4])

print(idlist)
with open("geop_idlist.txt", "w", encoding="utf-8") as f:
    f.write(str(idlist))
    f.close()
