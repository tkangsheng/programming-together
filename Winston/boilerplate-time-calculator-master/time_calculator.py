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
# convert duration into total minutes
# add the duration to the total minutes since 12AM (start time)
# count the number of + days. subtract the minutes * minutes per day
# starting minutes + duration minutes = new_time minutes
# then convert back.
# new_time minutes / (number of minutes in 1 day) = number of days R (minutes after 12AM on the last day)
# minutes after 12AM / (number of minutes in 1 hour) = number of hours after 12AM R (number of minutes after that hour)
    return new_time

result = add_time("3:00 PM", "3:10")
if result == "6:10 PM":
    print('correct')
else:
    print('incorrect')