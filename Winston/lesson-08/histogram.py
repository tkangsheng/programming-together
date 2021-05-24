nameList = ["winston", "grace", "winston", "sasha", "michelle", "kang sheng"]

histogram = dict()


for name in nameList:
    # if name in histogram:
    #     histogram[name] = histogram[name] + 1
    # else:
    #     histogram[name] = 0 + 1
    histogram[name] = histogram.get(name, 0) + 1

print(histogram)


bag = { "candy":1, "money": 2 }
result = None
if "candy" in bag:
    result = bag["candy"]
else:
    result = 20
print(result)

getResult = bag.get("candy", 20)
print(getResult)