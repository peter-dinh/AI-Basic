import numpy as np
import random

matrix = (
[0, 20, 42, 31, 6, 24],
[10, 0, 17, 6, 35, 18],
[25, 5, 0, 27, 14, 9],
[12, 9, 24, 0, 30, 12],
[14, 7, 21, 15, 0, 38],
[40, 15, 16, 5, 20, 0])

array = []


def GTS1( start):
    array.append(start)
    cost = 0
    u = start
    index = start

    while array.__len__()  != 6:
        min =1000000
        for v in range(0,6):
            if v not in array and v != u and matrix[u][v] < min and matrix[u][v] != 0:
                min = matrix[u][v]
                index = v
        u = index
        cost = cost + min
        array.append(index)

    print (cost + matrix[array[5]][start])
    array.append(start)
    print (array)
    for xx in array:
        print ("{} ==> ".format(xx+1))

list_ramdom = []

def GTS2():
    p = int(input("Nhap p:"))
    for item in range(p):
        while True:
            index_ram = random.randint(0,5)
            if index_ram not in list_ramdom:
                list_ramdom.append(index_ram)
                break
    print(list_ramdom)

    for x in list_ramdom:
        array.clear()
        print(x)
        GTS1(x)

(('0', 'Đồng đoàn'), ('1', 'Bạc đoàn'), ('2', 'Vàng đoàn'), ('3', 'Bạch kim đoàn'), ('4', 'Cao thủ đoàn'), ('5', 'Thách đấu đoàn'))
GTS1(1)
GTS2()
