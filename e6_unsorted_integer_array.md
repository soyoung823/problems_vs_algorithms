1. Problem explanations
The goal is to find the smallest and largest integer from a list of unsorted integers. 
The code should run in O(n) time. Do not use Python's inbuilt functions.

2. Complexity explanations
Time complexity: O(n)
    Total number of comparison:
        worst case: 1 + 2(n - 2) when the array is sorted in descending order.
        best case: 1 + n - 2 when the array is sorted in ascending order.

Space complexity: O(1) since the procedure only uses constant tuple.