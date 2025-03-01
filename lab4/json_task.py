import json


print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
with open('/Users/kadera/PP2/lab4/data.json', 'r') as f:
    file = json.load(f)
    for i in file['imdata']:
            print(i["l1PhysIf"]['attributes']['dn'], '                             ', i["l1PhysIf"]['attributes']['speed'], '', i["l1PhysIf"]['attributes']['mtu'])