import os
import csv

def set_all_rows(directory):
    """
        input: given a directory name
        output: the code will take all the csv files, turn every row into a dictionary and append that to a list. Then the list will be returned
    """
    all_rows = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.csv'):
            file_path = os.path.join(directory,filename)
            csv_file = csv.DictReader(open(file_path))
            for row in csv_file:
                all_rows.append(row)
    return all_rows

def filter_rows(rows, all_columns, main_column):
    filtered_rows = []
    for entry in rows:
        already_in = False
        for cols in filtered_rows:
            if cols[main_column] == entry[main_column]:
                # already in the list
                already_in = True
                for current_column in all_columns:
                    if current_column in cols and current_column in entry and cols[current_column] != entry[current_column]:
                        cols[current_column] += '\n\n'+entry[current_column]
                    else:
                        continue
        if already_in == False:
            filtered_rows.append(entry)
        # print(already_in)
    return filtered_rows

def generate_csv_from_data(output_csv_file, csv_columns, dict_data):
    try:
        with open(output_csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
        print("done..")
    except IOError:
        print("I/O error")

    

__version__ = '1.0'