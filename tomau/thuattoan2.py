import operator
# Vi du 1.7
# read file
file_obj = open("test2.txt", "r")
dinh = int(file_obj.readline())
canh = int(file_obj.readline())

matrix = [[ 0 for x in range(dinh)] for y in range(dinh)]
for i in range(0, canh):
    line = file_obj.readline()
    x , y  = line.split(" ")
    matrix[int(x)-1][int(y) - 1] = 1
    matrix[int(y) - 1][int(x) - 1] = 1

# sap xep bac cua dinh
list_bac = []
list_sort = []
list_color = []
for i in range(0, dinh):
    count = 0 
    for j in range(0, dinh):
        if matrix[i][j] == 1:
            count = count + 1
    list_bac.append(count)

for i in range(0, len(list_bac)):
    m = list_bac[i]
    x = [i, m]
    list_sort.append(x)

def getKey(item):
    return item[1]
list_sort.sort(reverse=True, key=getKey)

# To mau
dem = 0
while dem != dinh:
    list_tmp = []
    if not list_tmp:
        list_tmp.append(list_sort[0])

    for item in list_sort:
        check = 1
        for item_tmp in list_tmp:
            
            if matrix[item[0]][item_tmp[0]] == 1 or item_tmp[0] == item[0]:
                check = 0
    
        if check == 1:
            
            list_tmp.append(item)
    list_index = []
    for v in list_tmp:
        list_index.append(v[0])
        index = list_sort.index(v)
        list_sort.remove(list_sort[index])
    list_color.append(list_index)
    dem = dem + len(list_tmp)
    list_tmp.clear()

#ket qua + 1
print(list_color)
