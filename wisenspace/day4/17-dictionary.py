favorite_foods = {
    'Simon': 'pizza',
    'Jill': 'pancakes',
    'Roger': 'ramen'
}

# to see

print(favorite_foods)
print(favorite_foods['Roger'])

# add

favorite_foods['Alex'] = 'burger'
print(favorite_foods)

# deleting a item

del favorite_foods['Jill']
print(favorite_foods)

# keys and values

print(favorite_foods.keys())
print(favorite_foods.values())

# nested dictionary

world = {
    "america": [
        "usa",
        "canada",
        "mexico"
    ],
    "asia": [
        "korea",
        "china",
        "japan"
    ]
}
print(world)
print(world['america'][1])

cities = {
    'california': {
        'los angeles': {
            'population': 18790000
        },
        'san francisco': {
            'population': 884363
        }
    }
}

print(cities)
print(cities['california']['los angeles']['population'])

for key, val in world.items():
    print(f'{key} => {val}')

