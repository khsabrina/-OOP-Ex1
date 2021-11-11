import pandas as pd
import csv
import json
from Building import Building
from Elevator import Elevator
from callForElevator import callForElevator

if __name__ == '__main__':
 #c = pd.read_csv('Calls_a.csv' , header=None)
 #   print(c)

    f = open("f.json")
    data = json.load(f)
     # Creating a Building. Extracted from the json file
    B = Building(minFloor=data["_minFloor"], maxFloor=data["_maxFloor"])
    # print(data['_elevators'][0])
     # print(data['_elevators'][0]['_id'])
     # Creating the elevtors in the building
    for i in data['_elevators']:
        elev = Elevator(id=i['_id'], speed=i['_speed'], minFloor=i['_minFloor'], maxFloor=i['_maxFloor'],
                     closeTime=i['_closeTime'], openTime=i['_openTime'], startTime=i['_startTime'],
                     stopTime=i['_stopTime'])
        print(elev)
        print(elev.id)
        B.list_elvators.append(elev)

    for i in B.list_elvators:
        print(i)


    in_file = open("Calls_a.csv" )
    reader = csv.reader(in_file)
    out_file = open("out.csv","w",newline="")
    writer = csv.writer(out_file)
    for row in reader:
        row[5] = 4
        writer.writerow(row)
    in_file.close()
    out_file.close()
    #print(c.loc[:,1])
   # for i in c.loc[:,1]:
  #      print(i)
