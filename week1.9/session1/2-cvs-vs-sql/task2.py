with open("orders_export.csv", "r") as f:
    data = f.readlines()
    cleandata = []
    for line in data:
        cleandata.append(line.strip().split())
    print(cleandata)
