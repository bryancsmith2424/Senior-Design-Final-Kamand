from datetime import datetime, timedelta, time, timezone

def roundStartTo15(startTime):
    return startTime - timedelta(minutes = startTime.minute % 15) - timedelta(seconds = startTime.second, microseconds = startTime.microsecond)
def roundEndTo15(endTime):
    return endTime + timedelta(minutes = 15 - endTime.minute % 15) - timedelta(seconds = endTime.second, microseconds = endTime.microsecond)

#calander events must be ordered from earliest event to latest event
#have not tested with recurring events
def findAvailableTime(events, startDate, endDate, dayStartOffset, dayEndOffset, timeZoneOffset):
    availableTimes = []
    #sets start of day to 9am and end of day to 10pm, no avalible timeslots will be found outside these times
    #dayStartOffset and dayEndOffset can be used to change these default times based on user preference
    start = datetime.combine(startDate, time(9,0,0), timezone(timedelta(hours = timeZoneOffset)) ) + timedelta(hours = dayStartOffset)
    startTime = time(9 + dayStartOffset,0,0,0, timezone(timedelta(hours = timeZoneOffset)))
    end = datetime.combine(endDate, time(22,0,0), timezone(timedelta(hours = timeZoneOffset)) ) + timedelta(hours = dayEndOffset)
    endTime = time(22 + dayEndOffset,0,0,0, timezone(timedelta(hours = timeZoneOffset)))
    currTime = start
    if len(events['items']) > 0:
        firstEventStart = roundStartTo15(datetime.fromisoformat(events['items'][0]['start']['dateTime'])) - timedelta(minutes = 15)

        #find all the avalible time slots befor the first event
        while True:
            if firstEventStart < currTime + timedelta(minutes = 15):
                break
            else:
                if (currTime.timetz() >= startTime) and ((currTime + timedelta(minutes = 15)).timetz() <= endTime):
                    availableTimes.append((currTime, currTime + timedelta(minutes = 15)))
                currTime = currTime + timedelta(minutes = 15)
        #print("Got to first event")
        for i, event in enumerate(events['items']):
            currEventStart = roundStartTo15(datetime.fromisoformat(events['items'][i]['start']['dateTime'])) - timedelta(minutes = 15)
            if i == 0:
                currTime = roundEndTo15(datetime.fromisoformat(events['items'][0]['end']['dateTime'])) + timedelta(minutes = 15)
                continue
            while (currTime + timedelta(minutes = 15) <= currEventStart):
                if (currTime.timetz() >= startTime) and ((currTime + timedelta(minutes = 15)).timetz() <= endTime) and (currTime.date() == (currTime + timedelta(minutes = 15)).date()):
                    availableTimes.append((currTime, currTime + timedelta(minutes = 15)))
                currTime = currTime + timedelta(minutes = 15)
            if (currTime < roundEndTo15(datetime.fromisoformat(events['items'][i]['end']['dateTime'])) + timedelta(minutes = 15)):
                currTime =  roundEndTo15(datetime.fromisoformat(events['items'][i]['end']['dateTime'])) + timedelta(minutes = 15)

    #print("Got passed all events")
    while (currTime + timedelta(minutes = 15) <= end):
        if (currTime.timetz() >= startTime) and ((currTime + timedelta(minutes = 15)).timetz() <= endTime):
            availableTimes.append((currTime, currTime + timedelta(minutes = 15)))
        currTime = currTime + timedelta(minutes = 15)


    return availableTimes
