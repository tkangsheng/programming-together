MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = 24 * MINUTES_PER_HOUR

def add_time(start : str, duration : str, day_of_the_week = None):
    new_time = ''

    minutes_past_start_midnight = convert_AM_PM_to_minutes(start)
    duration_minutes = convert_hour_min_to_minutes(duration)
    end_minutes_past_start_midnight = minutes_past_start_midnight + duration_minutes

    days_past = end_minutes_past_start_midnight // MINUTES_PER_DAY
    end_minutes_past_start_midnight = end_minutes_past_start_midnight % MINUTES_PER_DAY
    end_hours = end_minutes_past_start_midnight // MINUTES_PER_HOUR
    if end_hours == 0:
        end_hours = 12
    elif end_hours > 12:
        end_hours = end_hours - 12

    am_pm = 'AM' if end_hours < 12 else 'PM'

    end_minutes = end_minutes_past_start_midnight % MINUTES_PER_HOUR

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

    if end_minutes < 10:
        end_minutes = f'0{end_minutes}'
    new_time = f'{end_hours}:{end_minutes} {am_pm}{weekday_text}{days_past_text}'

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
    weekday = weekday.capitalize()
    weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    new_weekday_index = (weekdays.index(weekday) + days_to_add) % len(weekdays)
    new_weekday = weekdays[new_weekday_index]
    return new_weekday

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "moNDay"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

print(add_time("7:30 PM", "18:00"))