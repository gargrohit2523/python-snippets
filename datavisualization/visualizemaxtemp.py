from pathlib import Path
import csv

path = Path("datasets\\delhi_temp_1951_2020.csv")
contents = path.read_text().splitlines()

reader = csv.reader(contents)
#read header row by calling next
header_row = next(reader)

highs = []

for row in reader:
    max_temp = 0
    try:
        max_temp = round(float(row[3]))
    except:
        pass
    highs.append(max_temp)

print(highs)