import requests
import bs4
import csv

def write_in_csv(file_name, data, header):
    with open(file_name, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(header)
        for std in data:
            spamwriter.writerow(std)

def load_data(site_path, class_name):
    resource = requests.get(site_path)
    site = bs4.BeautifulSoup(resource.content, "html.parser")
    table_head = site.select(class_name+" > thead > tr th")
    table_body = site.select(class_name+" > tbody > tr")
    table = []
    row_head = []
    for th in table_head:
        row_head.append(th.text[:])
    for tr in table_body:
        row = []
        for td in tr.select("td"):
            row.append(td.text[:])
        table.append(row)
    return row_head, table
def print_std(place):
    print(*row_head)
    for std in place:
        print(*std)
row_head,TABLE=load_data("https://data.uoi.ua/contest/uoi/2024/results",".table-striped")
place_I = []
place_II = []
place_III = []

for std in TABLE:
    if std[-1]=="I":
        place_I.append(std)
    elif std[-1]=="II":
        place_II.append(std)
    elif std[-1]=="III":
        place_III.append(std)

for i in range(len(place_I)):
    place_I[i][0]=i+1
for i in range(len(place_II)):
    place_II[i][0]=i+1
for i in range(len(place_III)):
    place_III[i][0]=i+1


write_in_csv("place_1.csv", place_I,row_head)
write_in_csv("place_2.csv", place_II,row_head)
write_in_csv("place_3.csv", place_III,row_head)



print("         I place")
print_std(place_I)
print("         II place")
print_std(place_II)
print("         place III")
print_std(place_III)