# Blog Notes: Quick Sort

## Pseudo Code
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

## Steps

Example List: [8,23,4,16]

- First Passthrough:
  > - left: 0, right: 3, list: [8,23,4,16], position:2
  > - We are passing in the list, the beginning index and the ending index into the quick_sort([8, 23, 4, 16], 0, len(list)-1)
  > - When passing the info into partition we receive a value of 2 back
  > - This 2 is then used in the recursive call that was made earlier
- Second Passthrough:
  > - left: 0, right: 1, list: [8,4,16,23], position:0
  > - We only have left = 0 still but right is now 1 while the list has been sorted with 16 and 23 being pushed to the end
  > - When passing the info into partition we will receive a position of 0 which will tell us to swap 8 and 4
  > - The 0 will be used in the recursive call
- Third Passthrough:
  > - left: 0, right: 1, list: [4,8,16,23], position: 0
  > - The final swapping happens here, leaving a fully sorted list.
