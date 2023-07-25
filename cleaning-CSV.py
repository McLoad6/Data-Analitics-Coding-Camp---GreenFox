import csv
import sys
import pandas
import copy

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
    csv_file = open(file_name, 'w')
    fieldnames = tuple(list[0])        
    writer = csv.writer(csv_file, fieldnames)
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
            number_list.append(value-1)
            new_list = column_request(sum_column)
            number_list.extend(new_list)
            return number_list
        else:
            new_list = column_request(sum_column)
            number_list.extend(new_list)
            return number_list

def choice_creator(choise_list:list, to_print:str):
    print("The following choise are:")
    x = 0
    for i in choise_list:
        x += 1
        print(f"{x} : {i}")
    print(to_print)
    return x

def column_selecter(csv_list:list, to_print:str):
    header = csv_list[0]
    x = choice_creator(header, to_print)
    selected_columns = column_request(x)
    return selected_columns

def filter_columns(csv_list:list):
    selected_columns = column_selecter(csv_list, "Choose columns which would you like to keep it. \nSelect the column NUMBER and press enter \nYou can set the order of the columns by choosing the desired order. \nFinish with 'q'")
    print("You choose the following columns in this order:")
    header = csv_list[0]
    for i in selected_columns:
        print(header[i])
    new_csv_list = []
    for row in csv_list:
        new_row = []
        for i in selected_columns:
            new_row.append(row[i])
        new_csv_list.append(new_row)
    write_list_to_csv("cleaned.csv", new_csv_list)

def column_values(column:list):
    elements = set()
    for value in column:
        elements.add(value)
    list_of_elements = list(elements)
    return list_of_elements

def value_selecter(unique_elements:list, to_print:str):
    x = choice_creator(unique_elements, to_print)
    selected_values = column_request(x)
    values = []
    for i in selected_values:
        values.append(unique_elements[i])
    return values

def filtering():
    cleaned_list = read_csv("cleaned.csv")
    selected_columns = column_selecter(cleaned_list, "Choose which column or columns want to filter:\nFinish with 'q'")
    for column in selected_columns:
        elements = []
        for row in cleaned_list:
            elements.append(row[column])
        elements.pop(0)
        unique_elements = column_values(elements)
        filtered_values = value_selecter(unique_elements, "Choose wich values want to keep it:\nFinish with 'q'")
        new_cleaned_list = []
        new_cleaned_list.append(cleaned_list[0])
        for i in range(1,len(cleaned_list)):
            if cleaned_list[i][column] in filtered_values:
                new_cleaned_list.append(cleaned_list[i])
        cleaned_list = copy.deepcopy(new_cleaned_list)
    write_list_to_csv("cleaned.csv", cleaned_list)


def main():
    csv_list = read_csv(get_file_name())
    filter_columns(csv_list)
    filtering()

if __name__ == "__main__":
    main()
