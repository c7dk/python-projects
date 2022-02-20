import json

# load the pokemon csv
pokedb = []
with open('../dat/pokemon.csv', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        parsed_oneline = line.split(',')
        pokedb.append(parsed_oneline)

# convert the 2d list to dictionary

poke_dict = {}
for mon in pokedb:
    poke_dict[mon[1]] = {
        'type': mon[2],
        'total': mon[3],
        'hp': mon[4],
        'attack': mon[5],
        'defense': mon[6],
        'sp atk': mon[7],
        'sp def': mon[8],
        'speed': mon[9]
    }

# save pokemon_dict json

with open('../dat/pokemon.json', 'w') as f:
    f.write(json.dumps(poke_dict, indent=4, sort_keys=True))
