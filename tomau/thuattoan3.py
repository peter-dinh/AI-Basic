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


list_bac = []
list_color = []
for i in range(0, dinh):
    count = 0 
    for j in range(0, dinh):
        if matrix[i][j] == 1:
            count = count + 1
    list_bac.append(count)

print(list_bac)