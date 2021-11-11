class callForElevator:
    def __init__(self,callTime, src, dst, idx):
        self.callTime = callTime
        self.src = src
        self.dst = dst
        self.idx =idx
        self.endTime = 0

    def __str__(self):
        print(self.callTime+", "+self.src+", "+self.dst)
        return ""