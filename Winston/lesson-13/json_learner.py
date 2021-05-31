import json

text = '''
{
    \"listA\": [123, \"treiwon\"]
}
'''

jObject = json.load('lesson-13/example.json')
jObject = json.loads(text)

listA = jObject['listA']
for item in listA:
    print(item)