1. Problem explanations
The goal is to implement the function to rearrange array elements to make 
two number such that their sum is maximum. Don't use inbuilt python function. 
The time complexity should be O(nlog(n)) when input size is n.

2. Complexity explanations.
Time complexity: O(nlog(n)) since we use quickSort to make time efficiency O(nlog(n))

Space complexity: O(log(n)) since the quickSort uses recursion for left and right partition respectively, the auxiliary stack O(long(n)) is used.