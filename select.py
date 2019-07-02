import os
import re

path1 = "d:/pubmed_data/seq/"
path2 = "d:/pubmed_data/select/"


for filename in os.listdir(path1):
    print(path1 + filename)
    with open(path1 + filename, encoding='utf-8') as f:
        for line in f.readlines():
            result = re.match('RNA', line, re.I)
            if result:
                print(result)
                with open(path1 + filename, encoding='utf-8') as f2:
                    for line in f2.readlines():
                        with open(path2 + filename, "a", encoding='utf-8') as f3:
                            f3.write(line)
                break
