import csv

field_names = ["Year", "Frequency"]
def split_data(filename):
    data = {}
    count = 0
    with open(filename, 'r',  encoding="utf-8") as f:
        datareader = csv.reader(f)
        for row in datareader:
            if count != 0:
                if row[7] not in data:
                    data[row[7]] = 1
                else:
                    data[row[7]] = data[row[7]] + 1 
            count+=1
    data2 =[]
    for key in data:
        data2.append((int(key), data[key]))    
        data2 = sorted(data2)  
    with open(r"public\finaldata\barByYear.csv", "w", newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['Year', 'Frequency'])
        for row in data2:
            csv_out.writerow(row)
            out.flush()



split_data("public\data_new.csv")