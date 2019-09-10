from Bio import Entrez

path = "d:/Eutils/geo/"
Entrez.email = "liqiming1914658215@gmail.com"
Entrez.api_key = "c80ce212c7179f0bbfbd88495a91dd356708"

# keywds: datatype


def search(database, keywords):
    handle = Entrez.esearch(db=database, term=keywords, retmax=13001)
    record = Entrez.read(handle)
    return record["Count"], record["IdList"]


def get_summary(database, geo_id):
    handle = Entrez.esummary(db=database, id=geo_id)
    record = Entrez.read(handle)
    return record[0]["Id"], record[0]["title"], record[0]["summary"]


def save_text(geo_id, title, summary):
    filename = path + geo_id + ".txt"
    print(filename)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("geo_id:\n\r"+geo_id+"\n\rTitle:\n\r"+title+"\n\rSummary:\n\r"+summary)


def main(database, keywords):
    count, idlist = search(database, keywords)
    print(count)
    flag = 0
    with open("idlist.txt", "w", encoding="utf-8") as f:
        f.write(str(idlist))
    for id in idlist:
        flag += 1
        with open("count_number.txt", "w", encoding="utf-8") as f:
            f.write(str(flag))
        geo_id, title, summary = get_summary(database, id)
        save_text(geo_id, title, summary)


if __name__ == '__main__':
    main("gds", "virus seq")
