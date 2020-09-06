'''
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. 
If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and 
your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:

Approach:
1. To find the pivot, divide the array in two sub-arrays and perform binary search.
    For a sorted (in increasing order) and pivoted array, 
    pivot element is the only element for which next element to it is smaller than it.
2. Pivot can be found by above statement and binary search.
3. After the pivot is found, divide the array in two sub-arrays.
4. The individual sub-arrays (left and right) are sorted so the element can be searched by binary search.

Pseudocode:
arr = [3, 4, 5, 1, 2]
search element = 1
    1. Find pivot and divide the array in two sub-arrays.
    pivot = len(arr) // 2
    2. call binary search for one of the two sub-arrays.
        a) If element > 0th element
            search in left array
        b) Else searcch in right array
    3. If element is found in selected sub-array
        return index
       Else
        return -1 
'''

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    n = len(input_list)
    pivot = findPivot(input_list, 0, n-1)

    # if pivot is noto found, array is not roated at all.
    if pivot == -1:
        return binarySearch(input_list, 0, n - 1, number)
    
    # if pivot is found, first compare with pivot and search i ntwo subarrays.
    if input_list[pivot] == number:
        return pivot
    if input_list[0] <= number:
        return binarySearch(input_list, 0, pivot - 1, number)
    return binarySearch(input_list, pivot + 1, n - 1, number)

# function to get pivot.
def findPivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)
    return findPivot(arr, mid + 1, high)

def binarySearch(arr, low, high, key):
    if high < low:
        return -1

    mid = int((low + high)/2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, mid + 1, high, key)
    return binarySearch(arr, low, mid - 1, key)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

