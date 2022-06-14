n = int(input("Enter the maximum number : "))
i = 0
value1 = 0
value2 = 1

while i < n:
    if i <= 1 :
        j = i
    else:
        j = value1 + value2
        value1 = value2
        value2 = j
    print(j)
    i = i + 1
