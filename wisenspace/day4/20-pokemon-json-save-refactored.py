import json

def load_csv(inpath):
    pokedb = []
    with open(inpath, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            parsed_oneline = line.split(',')
            pokedb.append(parsed_oneline)
    return pokedb

def convert(inlist):
    # convert 2d list to dictionary
    
    poke_dict = {}
    for mon in inlist:
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
    return poke_dict

def save_json(indict, savepath):
    with open(savepath, 'w') as f:
        # json.dump(indict, f)
        f.write(json.dumps(indict, indent=4, sort_keys=True))

def main():
    poke_list = load_csv('../dat/pokemon.csv')
    poke_dict = convert(poke_list)
    save_json(poke_dict, '../dat/pokemon.json')

if __name__ == "__main__":
    main()
