from csv_union import *


# The columns you want to scrap
columns = [
    'University',
    'Application Deadline',
    'Location',
    'Students',
    'Type',
    'Cost of Attendance',
    'Acceptance Rate',
    'SAT Range',
    'Ranking',
    'S:F ratio',
    'Application Fee',
    'Cool Things',
    'Programs',
    'Average Class Size',
    'SAT Subject Tests',
    'SAT Reporting',
    'Supplementary Writing (+ word count)',
    'Teacher Evaulations',
    'Other Evaluation',
    'ED II Date',
    'Interview?',
    'Supplementary Materials',
    'Setting',
    'Decisions Sent',
    'SAT Sent',
    'CSS Profile + FAFSA Sent',
    'Financial aid info',
    'Concerns',
    'Notes'
]

directory_name = 'csv_files'; # the directory where you'll put all the csv files

rows = set_all_rows(directory_name) #initial rows from all the spreadsheets

#filter themusing this function
filtered_rows = filter_rows(rows, columns, 'University') 

output_csv_file = 'final_spreadsheet.csv' #this is the output csv file name. it can be any name but make sure to use .csv extension

generate_csv_from_data(output_csv_file, columns, filtered_rows) #it'll generate the csv file

