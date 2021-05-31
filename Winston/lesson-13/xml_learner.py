import xml.etree.ElementTree as ET

data = '''
<person>
    <gender>Male</gender>
    <name>Chuck<language>English</language></name>
    <name>HuiSheng<language>Chinese</language></name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
nameValue = tree.find('name').text
print('Name:', nameValue)