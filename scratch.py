import json

with open("levels.vvvvvv", 'r') as levelarray:
    levels = json.loads(levelarray.read())

levels = [x for x in levels if x['monsterMayhem']=='True']
print(levels)