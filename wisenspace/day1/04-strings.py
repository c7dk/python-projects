first_name = 'Alexander'
last_name = 'Kang'

print(first_name)
print(last_name)

#string formatting

print(first_name + ' ' + last_name)
print(f'{first_name} {last_name}')

# assign it to new variable

full_name = first_name + ' ' + last_name
print(full_name)

# uppercase

print(full_name.upper())

# lowercase

print(full_name.lower())

# length

print(len(full_name))

# number to string

val = 10
converted = str(val)
print(converted)
print(type(converted))

# string to number

val = '-10'
converted = int(val)
print(converted)
print(type(converted))