import csv , json  # This is a sample Python script.
import struct

from barakElevator import Building
from barakElevator import callForElevator
from barakElevator import Elevator

import pandas as pd


def allocate(callList, B, output):
    out = []


    for i in callList:
        chosenElev = -1
        minTime = 1000
        for j in B.list_elvators:
                if(timecheck(i,j)<minTime):
                    minTime=timecheck(i,j)
                    chosenElev = j.id
        out.append(chosenElev)
        j.calls




    in_file = open("Calls_a.csv" )
    reader = csv.reader(in_file)
    out_file = open("out.csv","w",newline="")
    writer = csv.writer(out_file)
    i=0
    for row in reader:
        row[5] = out[i]
        writer.writerow(row)
        i=+1
    in_file.close()
    out_file.close()


def caniaddtothiselevator(call : callForElevator,elev : Elevator):
    for i in elev.calls:
        if (i.endTime<call.callTime):
            continue
        else:
            if(i.callTime<call.callTime):
                if(i.src==call.src):
                    return True
            if(i.dst==call.src):
                return True
            if(i.dir == call.dir):
                #if(i.dir==1):
                    if(i.callTime+timecheck(call,i) < call.callTime ):
                        return True
                #else:

    return False

def timecheck(call : callForElevator,elev : Elevator):
    return elev.closeTime+elev.startTime+(abs(call.src-call.dst))/elev.speed+elev.stopTime

def checkmytime(call : callForElevator,elev : Elevator ):
    if(elev.calls[-1]==None):
        return elev.closeTime + elev.startTime + (abs(call.src - 0)) / elev.speed + elev.stopTime + elev.openTime
    else:
        for i in elev.calls:



def Ex1(bld , calls , output):
    # Opening json file
    f = open(bld)
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
        B.list_elvators.append(elev)

    # print(B)
    #Closing the json file
    f.close()
    # Opening CSV file
    c = open(calls)
    csvreader = csv.reader(c)
    #Creating the callForElevators objects
    idx = 0
    callsList =[]
    for row in csvreader:
        call = callForElevator(row[1], row[2], row[3], idx)
        idx = +1
        callsList.append(call)

    #allocate(callsList, B, output)
    #Closing the CSV file
    c.close()

    with open(output, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['barak the king', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


if __name__ == '__barakmain__':
    Ex1('f.json', 'Calls_a.csv', 'out.csv')