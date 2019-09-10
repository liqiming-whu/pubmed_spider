import os

path1 = "d:/Eutils/data/"
path2 = "d:/Eutils/pmd/"
# virus viruses Virus Viruses viral Viral

for filename in os.listdir(path1):
    print(path1 + filename)
    with open(path1 + filename, encoding='utf-8') as f:
        for line in f.readlines():
            if "seq" in line:
                print("virus")
                if not os.path.exists(path2 + filename):
                    with open(path1 + filename, encoding='utf-8') as f2:
                        for line in f2.readlines():
                            with open(path2 + filename, "a",
                                      encoding='utf-8') as f3:
                                f3.write(line)
                break
