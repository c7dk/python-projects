list1 = ['a', 'b', 'c', 'd']
list2 = ['e', 'f']

# write a function to compare the 2 lists. 
# If they have a common element return true. If not return false

def compareList(list1, list2):
    for letter in list1:
        print(letter)

        for letter2 in list2:
            print(letter2)

            if letter == letter2:
                return True

    print('the end')
    return False

print(compareList(list1, list2))


# print(compareList(list1, list2))

# list3 = ['a', 'b', 'c', 'd']
# list4 = ['a', 'b', 'c', 'd']

# print(compareList(list3, list4))

# print(list1[0])