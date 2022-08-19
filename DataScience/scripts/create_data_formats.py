## Helper script to create data formats for the data files.
## Creates json, tsv from csv files.

import csv

with open("./data/the_office/the_office_lines.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    line_count = 0
    for line in reader:
          if line_count == 0:
               print(f'Column names are {", ".join(line)}')
               line_count += 1
          else:     
               line_count += 1
        