## 1. Bubble sort:

```c 
procedure bubbleSort(array A of size n)
    for i = 0 to n-1
        for j = 0 to n-i-1
            if A[j] > A[j+1]
                swap A[j] and A[j+1]
        end for
    end for
end procedure
```




### 2. Insertion Sort:
```c
procedure insertionSort(array A of size n)
    for i = 1 to n-1
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key
            A[j+1] = A[j]  // to emulate the place of i as j=i-1 
            j = j-1
        end while
        A[j+1] = key
    end for
end procedure
```




### 3. Selection Sort:


```c
procedure selectionSort(array A of size n)
    for i = 0 to n-1
        min_index = i
        for j = i+1 to n-1
            if A[j] < A[min_index]
                min_index = j
        end for
        if min_index != i
            swap A[i] and A[min_index]
    end for
end procedure
```



### 4. Quick Sort:

```c
procedure quickSort(array A, low, high)
    if low < high
        pivot_index = partition(A, low, high)
        quickSort(A, low, pivot_index-1)
        quickSort(A, pivot_index+1, high)
    end if
end procedure

procedure partition(array A, low, high)
    pivot = A[high]  
    i = low - 1   \\ means it starts from -1 (for low =0)
    for j = low to high-1
        if A[j] <= pivot
            i = i + 1
            swap A[i] and A[j]
        end if
    end for
    swap A[i+1] and A[high]     \\ default beahaviour ......... IDK !!!
    return i + 1
end procedure

```


 