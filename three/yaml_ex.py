import yaml

data1 = yaml.safe_load(open('data.yml'))
print(data1, type(data1))

data2 = yaml.safe_load(open('data2.yml'))
print(data2, type(data2))

data3 = yaml.safe_load(open('data3.yml'))
print(data3, type(data3))