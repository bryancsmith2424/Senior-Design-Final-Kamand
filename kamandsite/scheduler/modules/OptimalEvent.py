from datetime import datetime, timedelta, time, timezone

class OptimalEvent:
    def __init__(self, startTime, endTime, deadline, type, id, course, **kwargs):
        self.startTime = startTime
        self.endTime = endTime
        self.timeslotsOccupied = (endTime - startTime)//timedelta(minutes = 15)
        self.deadline = deadline
        self.type = type
        self.id = id
        self.course = course

        self.timeslots = []
        currTime = startTime
        for i in range(self.timeslotsOccupied):
            self.timeslots.append((currTime, currTime + timedelta(minutes = 15)))
            currTime += timedelta(minutes = 15)
        if not (self.timeslots[-1][1] == endTime):
            raise ValueError("Duration must be multiple of 15 minutes")

    def __repr__(self):
        return "{}:{} to {}".format(self.id, self.startTime, self.endTime)

    #need to define > = < etc.
    def __eq__(self, other):
        if (self.timeslotsOccupied == other.timeslotsOccupied and self.deadline == other.deadline and self.type == other.type):
            return True
        else:
            return False
    def __lt__(self, other):
        type_precednce_list = ['EX', 'QZ', 'HW',]
        if (self.type == other.type):
            if (self.deadline == other.deadline):
                if (self.timeslotsOccupied < other.timeslotsOccupied):
                    return True
                else:
                    return False
            else:
                if (self.deadline > other.deadline):
                    return False
                else:
                    return True
        else:
            if (type_precednce_list.index(self.type) < type_precednce_list.index(other.type)):
                return True
            else:
                return False
    def __gt__(self, other):
        type_precednce_list = ['EX', 'QZ', 'HW',]
        if (self.type == other.type):
            if (self.deadline == other.deadline):
                if (self.timeslotsOccupied < other.timeslotsOccupied):
                    return False
                else:
                    return True
            else:
                if (self.deadline > other.deadline):
                    return True
                else:
                    return False
        else:
            if (type_precednce_list.index(self.type) < type_precednce_list.index(other.type)):
                return False
            else:
                return True
