def spiral_matrix(size):
    matrix = [[("-") for i in range(size)] for i in range(size)]
    holder = 1
    index_holder = (0,0)
    behaviour = ("INCREMENT","ROW")
    while any(any(a == '-' for a in line) for line in matrix):
        x,y = index_holder

        matrix[y][x] = holder

        holder += 1


        if behaviour == ("INCREMENT","ROW"):
            if (x + 1 >= size or matrix[y][x+1] != "-") and y + 1 < size and matrix[y+1][x] == "-":
                index_holder = (x,y+1)
                behaviour = ("INCREMENT","COLUMN")
            else:
                index_holder = (x+1,y)
        
        elif behaviour == ("INCREMENT","COLUMN"):
            if (y + 1 >= size or matrix[y+1][x] != '-') and x -1 >= 0 and matrix[y][x-1] == "-":
                index_holder = (x-1,y)
                behaviour = ("DECREMENT","ROW")
            else:
                index_holder = (x,y+1)

        elif behaviour == ("DECREMENT","ROW"):
            if (x - 1 < 0 or matrix[y][x-1] != '-') and y - 1 >= 0 and matrix[y-1][x] == '-':
                index_holder = (x,y-1)
                behaviour = ('DECREMENT','COLUMN')
            else:
                index_holder = (x-1,y)

        elif behaviour == ('DECREMENT','COLUMN'):
            if (y - 1 < 0 or matrix[y-1][x] != '-') and x + 1 < size and matrix[y][x+1] == "-":
                index_holder = (x+1,y)
                behaviour = ("INCREMENT","ROW")
            else:
                index_holder = (x,y-1)
    return matrix

a = spiral_matrix(2)
for line in a:
    print(line)
