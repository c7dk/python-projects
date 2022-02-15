#variable way

rockets_player_1 = 'Rory'
rockets_player_1 = 'Rav'
rockets_player_1 = 'Rachel'
planets_player_1 = 'Peter'
planets_player_1 = 'Pablo'
planets_player_1 = 'Polly'

# --------------
# 1. create lists

rockets_player = ['Rory', 'Rav', 'Rachel']
planets_player = ['Peter', 'Pablo', 'Polly']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = ['math', 'english', 1997, 2000]

# ---------------
# 2. access values in lists

print(rockets_player[2])
print(planets_player[0])
print(list3[1:3])

# ---------------
# 3. updating the list

rockets_player[2] = 'Robin'
print(rockets_player)

# ---------------
# 4. append

rockets_player.append('Rocky')
print(rockets_player)
print(len(rockets_player))

# ---------------
# 5. loop through the list

for player in rockets_player:
    print(player)

for player in planets_player:
    print(player)

# ---------------
# 6. delete the element
# remove => remove by value

rockets_player.remove('Rav')
print(rockets_player)

# pop => remove from the back

rockets_player.pop()
print(rockets_player)

# del => remove by index

del rockets_player[1]
print(rockets_player)

# clear => delete all members

rockets_player.clear()
print(rockets_player)

# -----------------
# 7. operations

ret = len([1, 2, 3]) # length
print(ret)

ret = [1, 2, 3] + [4, 5, 6] # concat
print(ret)

ret = ['hi'] * 4 # repeat
print(ret)

ret = 3 in [1, 2, 3] # membership
print(ret)

# ------------------
# 8. indexing, slicin
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(colors[4])
print(colors[-1])
print(colors[-2])
print(colors[1:3])
print(colors[5:])

# -------------------
# 9. built in functions
print(max(list2))
print(min(list2))

list2.reverse()
print(list2)

list2.sort()
print(list2)