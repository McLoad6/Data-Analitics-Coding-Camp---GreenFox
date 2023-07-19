import csv
import sys

def read_csv(file):
    csv_list = []
    try: 
        my_file = open(file)
        try:
            content = csv.reader(my_file)
            for line in content:
                csv_list.append(line)
        finally:
            my_file.close()
    except OSError:
        sys.exit("I did not find the file")
    else:
         return csv_list
    
def write_dict_to_csv(file_name, list):
    csv_file = open(file_name, 'w')         #fontos formázni a file mengnyitását 'w'
    fieldnames = tuple(list[0].keys())        
    
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    
    for dict in list:
        writer.writerow(dict)
    
    csv_file.close()

def get_file_name():
    file_name = input("What CSV file would you like to open: ")
    dots = file_name.count(".")
    if dots == 1:
        if file_name[-4:] != ".csv":
            print("This is not CSV file! ")
            file_name = get_file_name()
    elif dots == 0:
        file_name = file_name + ".csv"
    else:
        print("Invalid file name! ")
        file_name = get_file_name()
    return file_name


print(read_csv(get_file_name()))

