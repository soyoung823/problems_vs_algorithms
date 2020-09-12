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
    # set all pointers start, mid, end for 0, 1, 2
    start_i = 0
    current_i = 0
    end_i = len(input_list) - 1

    # until current index <= end index
    while current_i <= end_i:

        # case 1: current_i element is 0
        if input_list[current_i] == 0:
            temp = input_list[start_i]
            input_list[start_i] = input_list[current_i]
            input_list[current_i] = temp
            start_i += 1
            current_i += 1

        # case 2: current_i element is 1
        elif input_list[current_i] == 1:
            current_i += 1

        # case 3: current_i element is 2
        elif input_list[current_i] == 2:
            temp = input_list[end_i]
            input_list[end_i] = input_list[current_i]
            input_list[current_i] = temp
            end_i -= 1

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
test_function([])
test_function([0])