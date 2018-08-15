# working
# intA = [9, 2, 1, 4, 6, 5, 7, 8]
f = open("data.txt", "r")
intA = (f.readline().split(','))
inputB = []
for i in intA:
    inputB.append(int(i))
intA = inputB
print("input array is ", intA)


def mergeSort(intA, startI, endI):
    # if endI - startI < 2:
    #     return  # least split
    if startI < endI:
        midI = (startI + endI) // 2
        mergeSort(intA, startI, midI)
        mergeSort(intA, midI + 1, endI)
        merge(intA, startI, midI, endI)


def merge(intA, startI, midI, endI):
    leftSplit = intA[startI:midI + 1]
    rightSplit = intA[midI + 1:endI + 1]
    tempI = startI
    i = j = 0
    while i < len(leftSplit) and j < len(rightSplit):
        if leftSplit[i] <= rightSplit[j]:
            intA[tempI] = leftSplit[i]
            i += 1
        else:
            intA[tempI] = rightSplit[j]
            j += 1
        tempI += 1  # one of split is done
    while i < len(leftSplit):
        intA[tempI] = leftSplit[i]
        i += 1
        tempI += 1
    while j < len(rightSplit):
        intA[tempI] = rightSplit[j]
        j += 1
        tempI += 1  # both done


mergeSort(intA, 0, len(intA) - 1)
print("Sorted array is  ", intA)
out = open("output.txt", 'w')
for i in intA:
    out.write(str(i) + ", ")
