import csv


def read_data():
    with open("virnaDB.txt", encoding="utf-8") as f:
        line_list = []
        for line in f.readlines():
            line = line.replace('\n', '')
            word_list = line.split("    ")
            line_list.append(word_list)
    return line_list


def create_csv(line_list):
    with open('virnadb.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for c in line_list:
            print(c)
            writer.writerow(c)


def main():
    line_list = read_data()
    create_csv(line_list)


if __name__ == '__main__':
    main()
