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

field_names = ["Country", "Frequency"]
american_countries = [
    "Canada", "United States", "Mexico", "Bahamas", "Cuba", "Jamaica", "Haiti",
    "Dominican Republic", "Puerto Rico", "Belize", "Guatemala", "El Salvador",
    "Honduras", "Costa Rica", "Nicaragua", "Panama",
    "Brazil", "Argentina", "Colombia", "Peru", "Venezuela", "Chile", "Ecuador",
    "Bolivia", "Paraguay", "Uruguay", "Guyana", "Suriname", "French Guiana"
]
def split_data(filename):
    data = {}
    count = 0
    with open(filename, 'r',  encoding="utf-8") as f:
        datareader = csv.reader(f)
        for row in datareader:
            if count != 0:
                for term in string_to_list(row[14]):
                    for country in american_countries:
                        if country in term:
                            if country not in data:
                                data[country] = 1
                            else:
                                data[country] = data[country] + 1  
            count+=1
        data2 =[]
    for key in data:
        data2.append((key, data[key]))    
        data2 = sorted(data2)  
    with open(r"D:\PanDiaspora\pandiaspora_shiny\Data\barByCountry.csv", "w", newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(field_names)
        for row in data2:
            csv_out.writerow(row)
            out.flush()

split_data(r"D:\PanDiaspora\pandiaspora_shiny\Rawdata\data_new.csv")