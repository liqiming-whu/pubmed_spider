import csv


path = "d:/Eutils/"


def get_id(path):
    with open(path+"geop_idlist.txt", encoding="utf-8") as f:
        idlist = eval(f.read())

    return idlist


def create_csv(idlist, path):
    with open(path+"geovirna.csv", "w",
              newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['geo_id', 'pubmed_id', 'virus', 'host',
                         'time', 'treatment', 'data', 'year', 'species'])
        for id in idlist:
            c = [id]
            print(c)
            writer.writerow(c)


def main():
    idlist = get_id(path)
    create_csv(idlist, path)


if __name__ == "__main__":
    main()
