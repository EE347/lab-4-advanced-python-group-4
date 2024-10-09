name = input("What is your name? ")

with open("task3.txt", "a") as file:
    file.write(name + "\n")