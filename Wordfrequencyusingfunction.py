def printChar(arr, Len):
    dict = {}
    for i in range(Len):
        if (arr[i] in dict):
            dict[arr[i]] = dict[arr[i]] + 1
        else:
            dict[arr[i]] = 1
    size = len(dict)
    while (size > 0):
        currentMax = 0
        arg_max = 0
        for key, value in dict.items():
            if (value > currentMax or (value == currentMax and key > arg_max)):
                arg_max = key
                currentMax = value
        print(f"{arg_max} - {currentMax}")
        dict.pop(arg_max)
        size -= 1
Str = input("Please enter a string : ")
Len = len(Str)
printChar(list(Str), Len)
