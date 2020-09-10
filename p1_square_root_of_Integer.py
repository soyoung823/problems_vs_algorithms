'''
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. 
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:

Try with all-natural numbers starting from 1.
Increment the number until its square root >= number.

Algorithm:
    1. Create a variable (counter) i and take care of some base cases,
    i.e when the given number is 0 or 1.
    2. Run a loop until i * i <= n, where n is the given number. Increment i by 1.
    3. The floor of the square root of the number is i - 1.

'''

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root

    # O(n)
    if number <= 1:
        return number
    i = 1
    result = 1
    while result <= number:
        i += 1
        result = i * i
    return i - 1
    """
    # edge case
    if number <= 1:
        return number

    low = 1
    high = number
    while low <= high:
        mid = (low + high) // 2
        
        if mid * mid == number:
            return mid
        if mid * mid < number:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1

    return ans

 
print ("Pass" if  (-1 == sqrt(-1)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1000 == sqrt(1000000)) else "Fail")
