from datetime import datetime

class Event:
    def __init__(self, startTime, endTime, type, id, dict = {}, **kwargs):
        self.startTime = startTime
        self.endTime = endTime
        self.type = type
        self.id = id
        self.dict = dict


        '''
        if (self.type == None):
            self.parseType()
        if ((kwargs.get('type') != None)):
            self.type = kwargs['type']
        else:
            self.parseType()
        '''

    def __repr__(self):
        return self.dict['summary']


    def createDict(self):
        eventDict = {
         'summary': '{}'.format(self.id),
         'description': 'We can make this part some tips/tricks based on the type (ex. Finding a good place to study...)',
         'start': {
           'dateTime': self.startTime.isoformat(),
           'timeZone': 'America/New_York',
         },
         'end': {
           'dateTime': self.endTime.isoformat(),
           'timeZone': 'America/New_York',
         },
         'reminders': {
           'useDefault': False,
           'overrides': [
              {'method': 'popup', 'minutes': 15},
           ],
         },
        }
        return eventDict

    def addToGoogleCalander(self, service, calendarID):
        service.events().insert(calendarId=calendarID, body=self.createDict()).execute()

    '''
    def getDuration(self):
        return duration

    def setDuration(self, duration):
        self.duration = duration

    def parseDuration(self):
        try:
            start = datetime.fromisoformat(self.dict['start']['dateTime'])
            end = datetime.fromisoformat(self.dict['end']['dateTime'])
            duration = end - start
            self.duration = duration
        except:
            self.duration = None
    '''
    def getType(self):
        return self.type
    def setType(self, type):
        self.tpye = type
    def parseType(self):
        eventName = self.dict['summary']
        wordsInEventName = eventName.split(' ')
        for word in wordsInEventName:
            if (word == 'Class') or (word == 'CLASS') or (word == "class"):
                self.type = "CLASS"
                return
        self.type = None

    def setDict(self, summary, start, end, **kwargs):
        return None
'''
    eDict = {
     'summary': 'Senior Design Project Class',
     'location': 'Busch?',
     'description': 'Making events with Googles API isn\'t that hard',
     'start': {
       'dateTime': '2020-03-10T18:00:00',
       'timeZone': 'America/New_York',
     },
     'end': {
       'dateTime': '2020-03-10T19:00:00',
       'timeZone': 'America/New_York',
     },
     'attendees': [
       {'email': 'mpardonner@gmail.com'},
       {'email': 'enilnoswerdna@gmail.com'}
     ],
     'reminders': {
       'useDefault': False,
       'overrides': [
         {'method': 'email', 'minutes': 24 * 60},
         {'method': 'popup', 'minutes': 15},
       ],
     },
    }
    event = Event(eDict)
    print(event.duration)
    print(event.type)
'''
