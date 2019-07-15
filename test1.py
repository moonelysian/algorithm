def maxMin(operations, x):
    arr = []
    maxMin = []
    for i in range(len(operations)):
        print(operations[i])
        print(x[i])
        if operations[i] is 'push':
            arr.append(x[i])
            print(arr)
        else:
            arr.remove(x[i])
            print(arr)
        maxMin.append(max(arr)*min(arr))
    print("maxMin: ",maxMin)
    return maxMin 

maxMin(['push','push','push','pop'],[1,2,3,1])