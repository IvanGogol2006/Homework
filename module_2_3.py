my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
b = (len(my_list))
#print(b)

while b-1 >= a:
    if my_list[a]>0:
        print(my_list[a])
        if my_list[a] == 0:
            continue
            print('0')
    a += 1
    if my_list[a] < 0:
        break