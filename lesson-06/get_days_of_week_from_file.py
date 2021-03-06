def get_lines_from_file(filePath):
    file = open(filePath)
    lines_starting_with_from = list()
    for each_line in file:
        if each_line.startswith("From "):
            lines_starting_with_from.append(each_line)
    return lines_starting_with_from

lines = get_lines_from_file("lesson-05\mbox-short.txt")

days_of_the_week = list()
index_of_weekday = 2
for each_line in lines:
    words = each_line.split()
    days_of_the_week.append(words[index_of_weekday])

print(days_of_the_week)

