from Bio import Entrez
from Bio import Medline

path = "d:/Eutils/data/"
Entrez.email = "liqiming1914658215@gmail.com"
Entrez.api_key = "c80ce212c7179f0bbfbd88495a91dd356708"

handle1 = Entrez.egquery(term="virus seq")
record1 = Entrez.read(handle1)
for row in record1["eGQueryResult"]:
    if row["DbName"] == "pubmed":
        count = row["Count"]
        print(count)

handle2 = Entrez.esearch(db="pubmed", term="virus seq", retmax=count)
record2 = Entrez.read(handle2)
handle2.close()
idlist = record2["IdList"]

handle3 = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = Medline.parse(handle3)
records = list(records)

for record in records:
    pmid = str(record.get("PMID", "?"))
    title = record.get("TI", "?")
    author = str(record.get("AU", "?"))
    abstract = record.get("AB", "?")
    source = record.get("SO", "?")
    filename = path + pmid + ".txt"
    print(filename)
    result = open(filename, "w", encoding="utf-8")
    result.write("title:\n\r")
    result.write(title)
    result.write("\n\rauthor:\n\r")
    result.write(author)
    result.write("\n\rabstract:\n\r")
    result.write(abstract)
    result.write("\n\rsource:\n\r")
    result.write(source)
    result.close()
