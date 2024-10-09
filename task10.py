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

growth_meta = (meta[-1] / meta[0])*100
growth_aapl = (aapl[-1] / aapl[0])*100
growth_amzn = (amzn[-1] / amzn[0])*100
growth_nflx = (nflx[-1] / nflx[0])*100
growth_nvda = (nvda[-1] / nvda[0])*100
growth_googl = (googl[-1] / googl[0])*100

plt.figure(figsize=(12,7))
plt.plot(dates, meta, label=f"META: +{growth_meta: .2f}%", color="b")
plt.plot(dates, aapl, label=f"AAPL: +{growth_aapl: .2f}%", color="gray")
plt.plot(dates, amzn, label=f"AMZN: +{growth_amzn: .2f}%", color="k")
plt.plot(dates, nflx, label=f"NFLX: +{growth_nflx: .2f}%", color="r")
plt.plot(dates, nvda, label=f"NVDA: +{growth_nvda: .2f}%", color="g")
plt.plot(dates, googl, label=f"GOOGL: +{growth_googl: .2f}%", color="orange")


plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("FAANNG Performance")
plt.legend()
plt.show()