import copy
from scheduler.modules.FindAvailableTime import findAvailableTime
from scheduler.modules.OptimalEvent import OptimalEvent
from scheduler.modules.Event import Event
from datetime import datetime, timedelta, time, date, timezone

def isEventTimeFeasible(optimalEvent, scheduledFirstTimeslot, availableTimes):
    scheduledFirstTimeslotIndex = availableTimes.index(scheduledFirstTimeslot)
    scheduledTimeslotsTaken = availableTimes[scheduledFirstTimeslotIndex : scheduledFirstTimeslotIndex + optimalEvent.timeslotsOccupied]
    if (optimalEvent.timeslotsOccupied != len(scheduledTimeslotsTaken)):
        return False
    for i in range(optimalEvent.timeslotsOccupied - 1):
        if(scheduledTimeslotsTaken[i][1] == scheduledTimeslotsTaken[i+1][0]):
            continue
        else:
            return False
    return True

def isDeadlineMet(event, scheduledEventEnd):
    if (event.deadline < scheduledEventEnd):
        return False
    return True



#availableTimes is the list of available timeslots from the findAvailableTime function
#eventsToAdd is the list of events we want to add to the schedule, should be ordered by importance
def greedyAlgo(availableTimes, eventsToAdd):
    originalAvailableTimes = copy.deepcopy(availableTimes)
    eventSchedule = []
    i = 0
    iterCount = 0
    while i < len(eventsToAdd) and iterCount < 500:
        iterCount += 1
        #print(i)
        #print(eventsToAdd)
        feasiblityCheck = False
        bestTimeDifference = 9999999999
        for slot in availableTimes:
            if (abs((eventsToAdd[i].startTime - slot[0]).total_seconds()) <= bestTimeDifference):
                scheduledFirstTimeslotIndex = availableTimes.index(slot)
                scheduledTimeslotsTaken = availableTimes[scheduledFirstTimeslotIndex : scheduledFirstTimeslotIndex + eventsToAdd[i].timeslotsOccupied]
                if isEventTimeFeasible(eventsToAdd[i], slot, availableTimes) and isDeadlineMet(eventsToAdd[i], scheduledTimeslotsTaken[-1][1]):
                    feasiblityCheck = True
                    bestTimeSlot = slot
                    bestTimeDifference = abs((eventsToAdd[i].startTime - slot[0]).total_seconds())


        #print(feasiblityCheck)
        if feasiblityCheck:
            scheduledFirstTimeslotIndex = availableTimes.index(bestTimeSlot)
            scheduledTimeslotsTaken = availableTimes[scheduledFirstTimeslotIndex : scheduledFirstTimeslotIndex + eventsToAdd[i].timeslotsOccupied]
            eventSchedule.append(Event(scheduledTimeslotsTaken[0][0], scheduledTimeslotsTaken[-1][1], eventsToAdd[i].type, eventsToAdd[i].id, eventsToAdd[i].course))
            for slot in scheduledTimeslotsTaken:
                availableTimes.remove(slot)
            i += 1
        else:
            event = eventsToAdd.pop(i)
            eventsToAdd.insert(i-1, event)
            eventSchedule = []
            availableTimes = copy.deepcopy(originalAvailableTimes)
            i = 0
    return eventSchedule
