

class Elevator:
    def __init__(self, id, speed="", minFloor: int = 0, maxFloor="", closeTime="", openTime="", startTime="",
                 stopTime="") -> None:
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.calls = []
        self.endcalls = []
        #self.missions = elevatorLinkedList()
        #self.missions.head = Node(0)
        #self.pos = 0


    def __str__(self) -> str:
        return f"id:{self.id} speed:{self.speed} minFloor:{self.minFloor} maxFloor:{self.maxFloor} closeTime:{self.closeTime} openTime:{self.openTime} StartTime:{self.startTime} stopTime:{self.stopTime}"

    def isEmpty(self):
        return (not self.call)


class Building:
    def __init__(self, minFloor, maxFloor):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.list_elvators = []

    def __str__(self) -> str:
        for i in self.list_elvators:
            print(i)
        return ""







class callForElevator:
    def __init__(self,callTime, src, dst, idx):
        self.callTime = callTime
        self.src = src
        self.dst = dst
        self.idx =idx
        self.endTime = 0
        self.onboard = 0
        if (dst-src>0):
            self.dir=1
        else:
            self.dir=-1

    def __str__(self):
        print(self.callTime+", "+self.src+", "+self.dst)
        return ""




# class Node:
#    def __init__(self, floor=None):
#        self.floor = floor
#        self.nextfloor = None
#
#
#
# class elevatorLinkedList:
#     def __int__(self):
#         self.head = None
#
#     def addhere(self, here, floor):
#         here.nextfloor = Node(floor)