import json

with open("levels.vvvvvv", 'r') as levelarray:
    levels = json.loads(levelarray.read())

levelFolder = "monstermayhemtest"
levels = [x for x in levels if x['folder']==levelFolder][0]['monsterMayhem']

print(levels)