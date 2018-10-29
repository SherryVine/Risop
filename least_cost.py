def create_table(row, column):
    array2d = []
    for i in range(row):
        array = []
        for j in range(column):
            val = int(input("value: "))
            array.append(val)
        array2d.append(array)
    for i in range(row):
        val = int(input("supply: "))
        array2d[i].append(val)
    demand = []
    for i in range(column):
        val = int(input("demand: "))
        demand.append(val)
    array2d.append(demand)
    return array2d

def print_table(row, column, table):
    for i in range(row+1):
        for j in range(column):
            print(table[i][j], end="\t")
            if(j+1 == column):
                if(i == row):
                    print()
                else:
                    print(table[i][column])
        #print()

def least_cost(row, column, table):
    array2d = []
    sort = []
    for i in range(row):
        array = []
        sort += sorted(table[i][:column])
        for j in range(column):
            array.append(0)
        array2d.append(array)
    sort = sorted(sort)
    i = 0
    cost_idx = 0
    hehe = 0    
    j = 0
    while(1):
        array = []
        while(1):
            if(table[i][j] == sort[cost_idx]):
                hehe = 0
                if(table[row][j] == 0):
                    cost_idx = cost_idx + 1        
                elif(table[i][column] >= table[row][j]):
                    array2d[i][j] = table[row][j]
                    table[i][column] -= table[row][j]
                    table[row][j] = 0
                    cost_idx = cost_idx + 1         
                    if(table[i][column] == 0):
                        j = j + 1
                        break
                elif(table[i][column] < table[row][j]):
                    array2d[i][j] = table[i][column]
                    table[row][j] -= table[i][column]
                    table[i][column] = 0
                    cost_idx = cost_idx + 1      
                    j = j + 1
                    break
            if(j+1 >= column):
                j = 0
                i = i + 1
                if(i == row):
                    i = 0
            else:
                j = j+1
            hehe = hehe + 1
        total = 0
        for k in range(column):
            total += table[row][k]
        if(total == 0):
            break    
    print("result: ", array2d)
    tot = 0
    for i in range(row-1):
        for j in range(column):
            tot += array2d[i][j]*table[i][j]
    print("total cost: ", tot)
#row = int(input("Jumlah baris: "))
#column = int(input("Jumlah kolom: "))
row = 3
column = 4
#table = create_table(row, column)
table = [[10,0,20,11,15], [12,7,9,20,25], [0,14,16,18,5], [5,15,15,10]]
minim = min(table)
print("min: ", min(minim))
print_table(row, column, table)
print()
lcm = least_cost(row, column, table)