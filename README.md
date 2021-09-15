# csv-union

Given a bunch of CSV files inside a directory, the code will be able to take all the entries from all the csv files and make a union of that data and insert them into a single csv file. Good for collecting unified survey data. 

# Pre-requirement

* Python-3 needs to be installed in your device (Check [https://www.python.org/downloads/](here) if you don't have python installed)

# Instruction

* Clone the project into your local machine. make sure python-3 is installed. open the `main.py` file and configure the columns list first. Put all the column names you want to scrap. I have set some samples. Feel free to edit that.

* Make a Directory in the root folder of the project. The directory name doesn't matter. You'll put all your CSV files inside that directory and update the `directory_name` variable in your `main.py` file. 

* `set_all_rows` function takes the `directory_name` and scraps all the entries from all the csv files inside that directory and returns a list of dictionaries in `rows` variable (You probably don't need to edit that line)

* `filter_all_rows` will take 3 parameters, initially scrappeond list (in this case the `row` variable), The columns you need to consider, and the main column that'll be used to filter the rows. So, suppose your `main_column` name is 'University'. Now, if two rows have exactly the same University, only one entry will be pushed. Any duplicates will be ignored. And if any column of this two entries have different entries, it'll store those entries with a newline. The following example should clarify everything. **I've given an example later in the docs, hope it'll make sense then.**

* After filtering the rows, just specify the output csv file and generaet csv from data where you'll give the output csv file name, columns and the filtered_rows and it'll create a csv file and put all the filtered_rows data there. **All the functions are inside `csv_union.py` in case you want to read them**

# Running the code

After finishing all the modifications, open a terminal/cmd and go to the root directory and run the following command: 

* for mac/linux, run `python3 main.py`
* for windows, run `python main.py`

# Example

### Imagine these are the initial rows and you want to filter the rows by University

| University      | People      | Size  | Good Stuff                                     |
| --------------- | ----------- | ----- | ---------------------------------------------- |
| Stanford University        | 4990        | Large | Literally one of the best schools in the world |
| Stanford University        | 4900        | Large | Amazing people                                 |
| Amherst College | 234 | Large | Need Blind LAC |
| Amherst College | 450 | Large | Amazing Courses |
| Columbia University | 200 | Large | New york, maaan |
| Amherst College | 234 | Large | One of the best Liberal Arts Colleges <br> #2 national Liberal Arts College |
| Amherst College | 450 | Large | Amazing Courses |
| Columbia University | 200 | Large | Amazing School |


### After running filter_all_rows, the above spreadsheet will look like this:

| University      | People      | Size  | Good Stuff                                     |
| --------------- | ----------- | ----- | ---------------------------------------------- |
| Stanford University       | 4990        | Large | Literally one of the best schools in the world <br> Amazing people |
| Amherst College | 234 <br> 450 | Large | Need Blind LAC <br> Amazing Courses <br> One of the best Liberal Arts Colleges <br> #2 national Liberal Arts College |
| Columbia University | 200 | Large | New york, maaan <br> Amazing School |