
## Quicksort
##inputA = [2,1,4,6,4,7]
f = open("data.txt", "r")
inputA = (f.readline().split(','))
##print(inputA)
inputB = []
for i in inputA:
	inputB.append(int(i))
inputA = inputB
print("input array is ", inputA)
length = len(inputA)

def partition(inputA, start, end):
	pivot = inputA[start]
	i = start
	j = end
	while (i<j):
		while(i<j):
			j-=1
			if(inputA[j]<pivot):
				break
		if(i<j):
			inputA[i] = inputA[j]
		while(i<j):
			i+=1
			if(inputA[i]>pivot):
				break
		if(i<j):
			inputA[j] = inputA[i]
	inputA[j]=pivot
	return j

def quickSort(inputA, start, end):
	if(end-start<2):
		return
	pivotIndex = partition(inputA, start, end)
	quickSort(inputA, start, pivotIndex)
	quickSort(inputA, pivotIndex+1, end)

quickSort(inputA, 0, length)
print("Sorted Array is ",inputA)
out = open("output.txt", 'w')
for i in inputA:
	out.write(str(i) + " ")
