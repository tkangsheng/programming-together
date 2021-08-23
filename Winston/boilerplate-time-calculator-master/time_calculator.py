def add_time(start, duration):
    new_time = ''
# split the start time into 3 parts. hours, mins, AM/PM
# confirm if minutes portion is < 60
# add duration's minutes to start time.
# convert 24 hrs into 1 day.
# convert 60 mins into 1 hour.

# after 11:59 AM -> 12:00 PM
# 11:59 PM -> 12:00 AM

# convert (start time) AM/PM to total minutes since 12:00AM
    start_minutes = convert_AM_PM_to_minutes(start)
    duration_minutes = convert_hour_min_to_minutes(duration)
# convert duration into total minutes
# add the duration to the total minutes since 12AM (start time)
# count the number of + days. subtract the minutes * minutes per day
# starting minutes + duration minutes = new_time minutes
# then convert back.
# new_time minutes / (number of minutes in 1 day) = number of days R (minutes after 12AM on the last day)
# minutes after 12AM / (number of minutes in 1 hour) = number of hours after 12AM R (number of minutes after that hour)
    return new_time

def convert_AM_PM_to_minutes(am_pm_time) -> int:
    [hours, minutes_am_pm] = am_pm_time.split(':')
    [minutes, am_pm] = minutes_am_pm.split(' ')
    hours = int(hours)
    minutes = int(minutes)
    minutes = minutes + hours*60
    if am_pm == 'AM':
        return minutes
    else: # am_pm == 'PM'
        minutes = minutes + 12*60
        return minutes

def convert_hour_min_to_minutes(hour_min) -> int:
    [hours, minutes] = hour_min.split(':')
    minutes = int(minutes)
    hours = int(hours)
    minutes = minutes + hours*60
    return minutes

print(convert_hour_min_to_minutes('2:32'))
print(convert_AM_PM_to_minutes('3:00 PM'))
result = add_time("3:00 PM", "3:10")
if result == "6:10 PM":
    print('correct')
else:
    print('incorrect')

