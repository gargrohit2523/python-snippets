from pathlib import Path
import csv
import matplotlib.pyplot as mplt
from datetime import datetime

path = Path("datasets\\delhi_temp_1951_2020.csv")

#read latest 2 year data by selecting last items from content which reduces data size and improves performance before plotting
contents = path.read_text().splitlines()[-730:]
reader = csv.reader(contents)
#read header row by calling next
header_row = next(reader)

highs = []
lows = []
dates = []

for row in reader:
    max_temp = 0
    min_temp = 0

    try:
        max_temp = round(float(row[3]))
        min_temp = round(float(row[4]))
    except:
        pass

    date = datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S')

    highs.append(max_temp)
    lows.append(min_temp)
    dates.append(date)

#mplt.style.use('seaborn')
figs,ax = mplt.subplots()

#Take last 2 years data from dataset
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='red', alpha=0.5)

#Give shading effect between y values i.e., high and lows for a date
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily High & Low Tempratures, 2019-2020, Delhi")

ax.set_xlabel('')
ax.set_ylabel("Temprature (C)")
figs.autofmt_xdate()

mplt.show()