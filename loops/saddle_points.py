def saddle_points(matrix):
    
    if matrix == []:
        return []

    if len(set(len(line) for line in matrix)) != 1:
        raise ValueError("irregular matrix")
    
    max_values = []
    fewer_values = []

    for i, line in enumerate(matrix):
        index_max_value = [index for index, value in enumerate(line) if value == max(line)]
        for value in index_max_value:
            max_values.append((i+1,value+1))

    for i in range(0,len(matrix[0])):
        column_values = []
        for j in range(0,len(matrix)):
            column_values.append(matrix[j][i])
        index_fewer_value = [index for index, value in enumerate(column_values) if value == min(column_values)]
        for value in index_fewer_value:
            fewer_values.append((value+1,i+1))

    good_spots = list(set(fewer_values).intersection(max_values))

    result = []

    for spot in good_spots:
        result.append({
            "row": spot[0],
            "column": spot[1]
        })

    return result

print(saddle_points([[1,6,3],
                     [3,4,2],
                     [3,5,1]]))


