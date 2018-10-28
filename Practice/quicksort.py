def partition(arr, start, end):
	i = start - 1  # i set to start -1
	pivot = arr[end]  # pivot is last
	for j in range(start, end):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[end] = arr[end], arr[i + 1]
	return i + 1


def quicksort(arr, start, end):
	if start < end:
		p = partition(arr, start, end)
		quicksort(arr, start, p - 1)
		quicksort(arr, p + 1, end)


arr = [3, 2, 5, 1, 4]
n = len(arr)
quicksort(arr, 0, n-1)
print(arr)
