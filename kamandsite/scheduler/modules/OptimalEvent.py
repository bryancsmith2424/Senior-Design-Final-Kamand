from datetime import datetime, timedelta, time, timezone

class OptimalEvent:
    def __init__(self, startTime, endTime, deadline, type, id, **kwargs):
        self.startTime = startTime
        self.endTime = endTime
        self.timeslotsOccupied = (endTime - startTime)//timedelta(minutes = 15)
        self.deadline = deadline
        self.type = type
        self.id = id

        self.timeslots = []
        currTime = startTime
        for i in range(self.timeslotsOccupied):
            self.timeslots.append((currTime, currTime + timedelta(minutes = 15)))
            currTime += timedelta(minutes = 15)
        if not (self.timeslots[-1][1] == endTime):
            raise ValueError("Duration must be multiple of 15 minutes")


    #need to define > = < etc.
