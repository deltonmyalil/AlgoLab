def merge(arr, start, mid, end):
	# define the temp lists and initialize them
	L = arr[:mid]
	R = arr[:mid]
	n1 = len(L)
	n2 = len(R)

	# merge the temp arrays
	i = 0
	j = 0
	k = start
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	# fill the leftovers
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1


def mergeSort(arr, start, end):
	if start < end:
		mid = (end - start) / 2
		mergeSort(arr, start, mid)
		mergeSort(arr, mid + 1, end)
		merge(arr, start, mid, end)


arr = [4, 2, 6, 1, 8]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
