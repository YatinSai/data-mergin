import csv

with open('data1.csv', newline="") as x:
  reader = csv.reader(x)
  data1 = list(reader)

with open('data2.csv', newline="") as y:
  reader = csv.reader(y)
  data2 = list(reader)

headers1 = data1[0]
headers2 = data2[0]
planet_data1 = data1[1:]
planet_data2 = data2[1:]

headers = headers1 + headers2
planet_data = []
for n in range(0,len(planet_data1)-1):
    planet_data.append(planet_data1[n] + planet_data2[n])
print(planet_data[0])

with open("merge.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(planet_data)


    
