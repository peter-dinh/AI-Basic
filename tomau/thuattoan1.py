import operator
# read file
file_obj = open("test.txt", "r")
dinh = int(file_obj.readline())
canh = int(file_obj.readline())

matrix = [[ 0 for x in range(dinh)] for y in range(dinh)]
for i in range(0, canh):
    line = file_obj.readline()
    x , y  = line.split(" ")
    matrix[int(x)][int(y)] = 1
    matrix[int(y)][int(x)] = 1


list_sort = []
list_color = []
for i in range(0, dinh):
    list_sort.append(i)


dem = 0
while dem != dinh:
    list_tmp = []
    if not list_tmp:
        list_tmp.append(list_sort[0])

    for item in list_sort:
        check = 1
        for item_tmp in list_tmp:
            
            if matrix[item][item_tmp] == 1 or item_tmp == item:
                check = 0
    
        if check == 1:
            
            list_tmp.append(item)
    list_index = []
    for v in list_tmp:
        list_index.append(v)
        index = list_sort.index(v)
        list_sort.remove(list_sort[index])
    list_color.append(list_index)
    dem = dem + len(list_tmp)
    list_tmp.clear()

print(list_color)