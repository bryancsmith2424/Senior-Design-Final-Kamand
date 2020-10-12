from scheduler.modules.OptimalEvent import OptimalEvent
from scheduler.modules.Event import Event
from datetime import datetime, timedelta, time, date, timezone

def myround(x, base=0.25):
    return base * round(x/base)

def createOptimalEvents(assignment_list, productive_time, tzoffset):
    if productive_time == 'EB':
        personal_optimal_time = time(6, 30)
    elif productive_time == 'MM':
        personal_optimal_time = time(9, 30)
    elif productive_time == 'MD':
        personal_optimal_time = time(12, 30)
    elif productive_time == 'AA':
        personal_optimal_time = time(15, 30)
    elif productive_time == 'EE':
        personal_optimal_time = time(18, 30)
    elif productive_time == 'NO':
        personal_optimal_time = time(21, 0)
    elif productive_time == 'NN':
        personal_optimal_time = time(0, 30)
    else:
        return "ERROR"

    optimal_event_list = []
    for assignment in assignment_list:
        if assignment.assignment_type == 'HW':
            if  assignment.time_to_complete_estimate < 1:
                duration = 1
            else:
                duration = assignment.time_to_complete_estimate
            start_time = datetime.combine(assignment.deadline.date() - timedelta(days=3), personal_optimal_time, tzinfo=tzoffset) - timedelta(hours=(duration/2.0))
            end_time = datetime.combine(assignment.deadline.date() - timedelta(days=3), personal_optimal_time, tzinfo=tzoffset) + timedelta(hours=(duration/2.0))
            optimal_event = OptimalEvent(start_time, end_time, assignment.deadline, 'HW', assignment.assignment_name)
            optimal_event_list.append(optimal_event)
        elif assignment.assignment_type == 'QZ':
            if  assignment.time_to_complete_estimate < 1:
                duration = 1
            else:
                duration = assignment.time_to_complete_estimate
            start_time = datetime.combine(assignment.deadline.date() - timedelta(days=1), personal_optimal_time, tzinfo=tzoffset) - timedelta(hours=(duration/2.0))
            end_time = datetime.combine(assignment.deadline.date() - timedelta(days=1), personal_optimal_time, tzinfo=tzoffset) + timedelta(hours=(duration/2.0))
            optimal_event = OptimalEvent(start_time, end_time, assignment.deadline, 'QZ', assignment.assignment_name)
            optimal_event_list.append(optimal_event)
        elif assignment.assignment_type == 'EX':
            if  assignment.time_to_complete_estimate < 3:
                duration = 1
            else:
                duration = myround(assignment.time_to_complete_estimate/3)
            start_time = datetime.combine(assignment.deadline.date() - timedelta(days=4), personal_optimal_time, tzinfo=tzoffset) - timedelta(hours=(duration/2.0))
            end_time = datetime.combine(assignment.deadline.date() - timedelta(days=4), personal_optimal_time, tzinfo=tzoffset) + timedelta(hours=(duration/2.0))
            optimal_event = OptimalEvent(start_time, end_time, assignment.deadline, 'EX', assignment.assignment_name)
            optimal_event_list.append(optimal_event)
            start_time = datetime.combine(assignment.deadline.date() - timedelta(days=3), personal_optimal_time, tzinfo=tzoffset) - timedelta(hours=(duration/2.0))
            end_time = datetime.combine(assignment.deadline.date() - timedelta(days=3), personal_optimal_time, tzinfo=tzoffset) + timedelta(hours=(duration/2.0))
            optimal_event = OptimalEvent(start_time, end_time, assignment.deadline, 'EX', assignment.assignment_name)
            optimal_event_list.append(optimal_event)
            start_time = datetime.combine(assignment.deadline.date() - timedelta(days=1), personal_optimal_time, tzinfo=tzoffset) - timedelta(hours=(duration/2.0))
            end_time = datetime.combine(assignment.deadline.date() - timedelta(days=1), personal_optimal_time, tzinfo=tzoffset) + timedelta(hours=(duration/2.0))
            optimal_event = OptimalEvent(start_time, end_time, assignment.deadline, 'EX', assignment.assignment_name)
            optimal_event_list.append(optimal_event)
    optimal_event_list.sort(reverse=True)
    return optimal_event_list
