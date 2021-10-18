hours_in_clock = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
AM_PM = ['AM', 'PM']

start = '8'
start_am_pm = 'PM'

end = hours_in_clock[(hours_in_clock.index(start) + 108) % len(hours_in_clock)]
end_am_pm = AM_PM[(AM_PM.index(start_am_pm) + (108//len(hours_in_clock))) % len(AM_PM)]
end_time = f'{end}{end_am_pm}'
print(end_time)