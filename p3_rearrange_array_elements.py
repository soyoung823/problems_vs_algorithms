'''
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. 
Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. 
Another expected answer can be [542, 31]. 
In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
'''

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) < 2:
        return [-1]

    # sort the input in descending order
    # input_list.sort(reverse=True)
    # quicksort. last element = pivot
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high] # last element

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(arr, low, high):
        if low < high:
            partitioning_i = partition(arr, low, high)

            quickSort(arr, low, partitioning_i - 1)
            quickSort(arr, partitioning_i + 1, high)

    n1 = ''
    n2 = ''

    for i in range(len(input_list)):
        if i % 2 == 0:
            n1 += str(input_list[i])
        else:
            n2 += str(input_list[i])
    return [int(n1), int(n2)]
'''
# merge sort the array
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_i = 0
    right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            merged.append(right[right_i])
            right_i += 1
        else:
            merged.append(left[left_i])
            left_i += 1

    merged += left[left_i:]
    merged += right[right_i:]

    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) < 2:
        return [-1]

    sorted_list = merge_sort(input_list)
    n1 = ''
    n2 = ''

    for i in range(len(sorted_list)):
        if i % 2 == 0:
            n1 += str(sorted_list[i])
        else:
            n2 += str(sorted_list[i])
    return [int(n1), int(n2)]
'''

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([None, [-1]])
test_function([[], [-1]])
test_function([[0], [-1]])
test_function([[0, 0], [0, 0]])
test_function([[9, 7, 8], [98, 7]])