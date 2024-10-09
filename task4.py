with open("task3.txt", "r") as file:
    names = file.readlines()

    for name in names:
        print(name)