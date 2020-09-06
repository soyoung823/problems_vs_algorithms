'''
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. 
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. 
For e.g. if you traverse the array twice, 
that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
'''

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # one pass + in-place
    # set all pointers start, cur, end for 0, 1, 2
    start = 0
    cur = 0
    end = len(input_list) - 1

    # until cur index <= end index
    while cur <= end:
        # case 1: cur element is 0
        if input_list[cur] == 0:
            input_list[cur], input_list[start] = input_list[start], input_list[cur]
            start += 1
            cur += 1
        # case 2: cur element is 1
        elif input_list[cur] == 1:
            cur += 1
        # case 3: cur element is 2
        elif input_list[cur] == 2:
            input_list[cur], input_list[end] = input_list[end], input_list[cur]
            end -= 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
