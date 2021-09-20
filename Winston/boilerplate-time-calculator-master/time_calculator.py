def add_time(start : str, duration : str, day_of_the_week = None):
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
# convert duration into total minutes
    duration_minutes = convert_hour_min_to_minutes(duration)
# add the duration to the total minutes since 12AM (start time)
    end_minutes = start_minutes + duration_minutes
# starting minutes + duration minutes = new_time minutes
# count the number of + days. subtract the minutes * minutes per day
    MINUTES_PER_HOUR = 60
    MINUTES_PER_DAY = 24 * MINUTES_PER_HOUR
    days_past = end_minutes // MINUTES_PER_DAY
# then convert back.
# new_time minutes / (number of minutes in 1 day) = number of days R (minutes after 12AM on the last day)
# minutes after 12AM / (number of minutes in 1 hour) = number of hours after 12AM R (number of minutes after that hour)
    new_time_minutes_past_midnight = end_minutes % MINUTES_PER_DAY
    new_time_hours = new_time_minutes_past_midnight // MINUTES_PER_HOUR

    am_pm = 'AM'
    if new_time_hours >= 12:
        am_pm = 'PM'

    if new_time_hours == 0:
        new_time_hours = 12
    elif new_time_hours > 12:
        new_time_hours = new_time_hours - 12

    new_time_minutes = new_time_minutes_past_midnight % MINUTES_PER_HOUR

    weekday_text = ''
    if day_of_the_week is not None:
        new_time_weekday = add_days(day_of_the_week, days_past)
        weekday_text = f', {new_time_weekday}'

    # if days_past == 0
    days_past_text = ''
    if days_past == 1:
        days_past_text = f' (next day)'
    elif days_past > 1:
        days_past_text = f' ({days_past} days later)'

    if new_time_minutes < 10:
        new_time_minutes = f'0{new_time_minutes}'
    new_time = f'{new_time_hours}:{new_time_minutes} {am_pm}{weekday_text}{days_past_text}'

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

def add_days(weekday : str, days_to_add : int):
    weekday = weekday.lower()
    weekday = f'{weekday[0].upper()}{weekday[1:].lower()}'
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_weekday_index = (weekdays.index(weekday) + days_to_add) % len(weekdays)
    new_weekday = weekdays[new_weekday_index]
    return new_weekday

print(add_time("8:18 PM", "100:00"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)