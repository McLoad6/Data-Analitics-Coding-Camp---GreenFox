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
    
def write_list_to_csv(file_name, list:list):
    csv_file = open(file_name, 'w')         #fontos formázni a file mengnyitását 'w'
    fieldnames = tuple(list[0])        
    writer = csv.writer(csv_file, fieldnames)
    #writer.writeheader()
    #list.pop(0)
    for row in list:
        writer.writerow(row)
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

def is_it_in_range(number_to_check, the_range):
    if number_to_check.isdigit():
        number_to_check = int(number_to_check)
        if number_to_check in range(1,the_range+1):
            return True
        else:
            print("No such a column.")
            return False
    else:
        print("Please give a NUMBER")
        return False

def column_request(sum_column:int):
    value = input(":")
    number_list = []
    if value == "q":
        return number_list
    else:
        if is_it_in_range(value, sum_column):
            value = int(value)
            number_list.append(value)
            new_list = column_request(sum_column)
            number_list.extend(new_list)
            return number_list
        else:
            new_list = column_request(sum_column)
            number_list.extend(new_list)
            return number_list

def column_selecter(csv_list:list):
    print("The following columns in the CSV:")
    header = csv_list[0]
    x = 0
    for i in header:
        x += 1
        print(f"{x} : {i}")
    print("Choose columns which would you like to keep it. \nSelect the column NUMBER and press enter \nYou can set the order of the columns by choosing the desired order. \nFinish with 'q'")
    selected_columns = column_request(x)
    print("You choose the following columns in this order:")
    for i in selected_columns:
        print(header[i-1])
    new_csv_list = []
    for row in csv_list:
        new_row = []
        for i in selected_columns:
            new_row.append(row[i-1])
        new_csv_list.append(new_row)
    print(new_csv_list)
    write_list_to_csv("cleaned.csv", new_csv_list)


def main():
    csv_list = read_csv(get_file_name())
    column_selecter(csv_list)

if __name__ == "__main__":
    main()
