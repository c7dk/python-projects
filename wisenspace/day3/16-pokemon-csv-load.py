"""
# ---
# 1 load the csv
with open('../dat/pokemon.csv', 'r') as f:
    print(f.read())
"""

# -------------------
# 2 parse the data

pokedb = []

with open('../dat/pokemon.csv', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        parsed_oneline = line.split(',')
        pokedb.append(parsed_oneline)

print(pokedb[0][1])
print(pokedb[4][3])

# ---------------------
# 3 list all names

for mon in pokedb:
    print(mon[1])

# ---------------------
# 4 filter only "Rock" Type

for mon in pokedb:
    # if 'BUG' in mon[2]:
    #   print(mon[1])
    # if total is bigger than 400
    if int(mon[3]) > 600:
        print(mon[1])
