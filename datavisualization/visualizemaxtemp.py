from pathlib import Path
import csv
import matplotlib.pyplot as mplt
from datetime import datetime

path = Path("datasets\\delhi_temp_1951_2020.csv")
contents = path.read_text().splitlines()

reader = csv.reader(contents)
#read header row by calling next
header_row = next(reader)

highs = []
dates = []

for row in reader:
    max_temp = 0

    try:
        max_temp = round(float(row[3]))
    except:
        pass

    date = datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S')

    highs.append(max_temp)
    dates.append(date)

#mplt.style.use('seaborn')
figs,ax = mplt.subplots()
ax.plot(dates[-30:], highs[-30:], color='red')

ax.set_title("Daily High Temprature, 2020 Last 2 months, Delhi")

ax.set_xlabel('')
ax.set_ylabel("Temprature (C)")
figs.autofmt_xdate()

mplt.show()