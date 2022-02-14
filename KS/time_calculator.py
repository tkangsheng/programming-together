def time_calculator(start : str, duration : str, day=None):

    start = start.split( )
    # Split start into hours & minutes

    start_hm = start[0].split(":")

    if start[1] == "PM":
        start_hr = int(start_hm[0]) + 12
    else:
        start_hr = int(start_hm[0])
    start_min = int(start_hm[1])

    # Split duration into hours & minutes
    duration_hm = duration.split(":")

    duration_hr = int(duration_hm[0])
    duration_min = int(duration_hm[1])

    # Add start and duration hour
    total_hr = start_hr + duration_hr

    # Add start and duration minutes, if > 60, add 1 to hours
    final_min = start_min + duration_min
    if final_min > 59: 
        total_hr = total_hr + final_min//60
        final_min = final_min % 60
    
    # Determine whether it's AM or PM.
    time_period = ''
    if (total_hr // 12) % 2 == 1:
        time_period = 'PM'
    else:
        time_period = 'AM'

    #Convert hr/min to str
    final_min = str(final_min)

    if len(final_min) == 1:
        final_min = "0" + final_min

    final_hr = str(total_hr % 12)

    #Change 0hrs to 12hrs
    if final_hr == "0":
        final_hr = "12"

    #determining the number of days past
    days_past = total_hr // 24
    
    #determine how many days later
    if days_past == 0:
        days_later = ''
    elif days_past == 1:
        days_later = ' (next day)'
    else:
        days_later = ' (' + str(days_past) + ' days later)'

    if day:
        # Define order in days of the week
        days = ['monday', 'tuesday', 'Wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_day = days.index(day.lower())
        
        final_day = days[(start_day + days_past) % 7].capitalize()
        # Final time
        final_time = final_hr + ':' + final_min + ' ' + time_period + ', ' + final_day + days_later
    else:
        final_time = final_hr + ':' + final_min + ' ' + time_period + days_later

    return final_time

print(time_calculator("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(time_calculator("11:30 AM", "2:32", "moNDay"))
# Returns: 2:02 PM, Monday

print(time_calculator("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(time_calculator("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(time_calculator("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(time_calculator("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

# unresolved:
# 1. Add (2 days later)/(next day)