def selection














def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i 
        for j in range (i+1,n):
            if arr[j]<arr[j+1]:
                min_index = j 
        arr