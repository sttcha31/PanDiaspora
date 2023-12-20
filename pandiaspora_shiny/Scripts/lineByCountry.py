import csv
import ast

def string_to_list(s):
    try:
        # Use ast.literal_eval to safely evaluate the string and convert it to a list
        result = ast.literal_eval(s)
        if isinstance(result, list):
            return result
        else:
            raise ValueError("Input is not a valid list")
    except (ValueError, SyntaxError):
        raise ValueError("Input is not in the correct format")

field_names = [
    "Year", "CAN", "USA", "MEX", "BHS", "CUB", "JAM", "HTI", "DOM", "PRI", "BLZ",
    "GTM", "SLV", "HND", "CRI", "NIC", "PAN", "BRA", "ARG", "COL", "PER",
    "VEN", "CHL", "ECU", "BOL", "PRY", "URY", "GUY", "SUR", "GUF"
]
american_countries = [
    "Canada", "United States", "Mexico", "Bahamas", "Cuba", "Jamaica", "Haiti",
    "Dominican Republic", "Puerto Rico", "Belize", "Guatemala", "El Salvador",
    "Honduras", "Costa Rica", "Nicaragua", "Panama",
    "Brazil", "Argentina", "Colombia", "Peru", "Venezuela", "Chile", "Ecuador",
    "Bolivia", "Paraguay", "Uruguay", "Guyana", "Suriname", "French Guiana"
]
def split_data(filename):
    data = {
        '2013': {},
        '2014': {},
        '2015': {},
        '2016': {},
        '2017': {},
        '2018': {},
        '2019': {},
        '2020': {},
        '2021': {},
        '2022': {},
        '2023': {},
        '2024': {},


    }   
    for key in data.keys():
        for countries in american_countries:
            data[key][countries] = 0
    count = 0
    with open(filename, 'r',  encoding="utf-8") as f:
        datareader = csv.reader(f)
        for row in datareader:
            if count != 0:
                for term in string_to_list(row[14]):
                    for country in american_countries:
                        if country in term:
                             try:
                                data[row[8]][country] = data[row[8]][country] + 1
                             except:
                                data[row[8]] = {}
                                data[row[8]][country] = 1
                                  
            count+=1
    data2 =[]
    for key in data.keys():
        temp = [key]
        for country in data[key]:
            temp.append(data[key][country])
        data2.append(temp)    
    with open(r"D:\PanDiaspora\pandiaspora_shiny\Data\lineByCountry.csv", "w", newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(field_names)
        for row in data2:
            csv_out.writerow(row)
            out.flush()

split_data(r"D:\PanDiaspora\pandiaspora_shiny\Rawdata\data_new.csv")