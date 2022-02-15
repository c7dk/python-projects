def bubble_sort(inp):
    for i in range(0, len(imp)):
        for j in range(i + 1, len(inp)):
            ei = inp[i]
            ej = inp[j]
            print(f'{i} {j} => {ei} {ej}')

            if(ei > ej):
                inp[i] = ej
                inp[j] = ei
                print('**** swap ****')

            print(inp)
            print('----')
    return inp
list1 = [44, 22, 77, 33, 99, 11]
ret = bubble_sort(list1)
print(ret) # [22, 33, 44, 77]

list1.sort()
print(list1)