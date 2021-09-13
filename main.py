from csv_union import *


# The columns you want to scrap
columns = [
    'Name',
    'Class',
    'Age',
    'Title',
    'Hudai'
]

directory_name = 'csv_files';
rows = set_all_rows(directory_name)
filtered_rows = filter_rows(rows, columns, 'Name')

output_csv_file = 'final_spreadsheet.csv'

generate_csv_from_data(output_csv_file, columns, filtered_rows)


#print(rows)
