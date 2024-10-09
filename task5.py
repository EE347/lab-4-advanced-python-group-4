import csv

with open("task5.csv", mode="w", newline='') as file:
    writer = csv.writer(file)

    while True:
        name = input("Enter your name: ")
        if name.lower() == "quit":
            break

        writer.writerow([name])

with open("task5.csv", mode="r") as file:
    reader = csv.reader(file)

    print("Names in file:")
    for row in reader:
        print(row[0])