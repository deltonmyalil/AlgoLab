intA = [9, 2, 1, 4, 6, 5, 7, 8]


def merge(intA, startI, midI, endI):
    if intA[midI - 1] <= intA[midI]:
        return
    i = startI
    j = midI
    tempI = 0
    tempA = []
    while i < midI and j < endI:
        if intA[i] <= intA[j]:
            tempA.append(intA[j])
            i += 1
            tempI += 1
        else:
            tempA.append(intA[j])
            j += 1
            tempI += 1
    arrayCopy(intA, i, intA, startI + tempI, midI)
    arrayCopy(tempA, 0, intA, startI, midI)


# same logic as System.arraycopy() in java
def arrayCopy(src, srcPos, dest, destPos, length):
    # for i in range(length-1):
    #     print(i, destPos, srcPos)
    # dest[i + destPos] = src[i + srcPos]
    dest[destPos:destPos + length] = src[srcPos:srcPos + length]


def mergeSort(intA, startI, endI):
    if endI - startI < 2:
        return
    midI = (startI + endI) // 2
    mergeSort(intA, startI, midI)
    mergeSort(intA, midI + 1, endI)
    merge(intA, startI, midI, endI)


mergeSort(intA, 0, len(intA) - 1)
print(intA)
# Not working, need to check
# list index out of range
