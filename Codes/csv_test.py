import csv

with open("flowers.csv", "r") as f:
    csv_f = csv.reader(f)
    for i in csv_f:
        print(i)
        #print(type(i))
        name, color, types = i
        print("The name is:{}, the type is:{}, the colour is:{}". format(name, color, types))
    flower_list = list(csv.reader(f))
    print(type(csv.reader(f)))
    print(type(flower_list))
    print(flower_list)
