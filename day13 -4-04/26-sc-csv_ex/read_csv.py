import csv

with open(r'D:\py_training\python-training\day13 -4-04\26-sc-csv_ex\data.csv','r') as f:
  data = csv.reader(f)
  print('DATA TYPE: ', type(data))
  for row in data:
        print(row)


reader = csv.DictReader(open(r"D:\py_training\python-training\day13 -4-04\26-sc-csv_ex\data.csv"))
for raw in reader:
    print(dict(raw))
