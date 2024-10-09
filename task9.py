import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates = []
meta = []
aapl = []
amzn = []
nflx = []
nvda = []
googl = []

with open("task9.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        date = datetime.strptime(row[0], "%d/%m/%Y")
        dates.append(date)
        meta.append(float(row[1]))
        aapl.append(float(row[2]))
        amzn.append(float(row[3]))
        nflx.append(float(row[4]))
        nvda.append(float(row[5]))
        googl.append(float(row[6]))

plt.plot(dates, meta)
plt.plot(dates, aapl)
plt.plot(dates, amzn)
plt.plot(dates, nflx)
plt.plot(dates, nvda)
plt.plot(dates, googl)
plt.show()