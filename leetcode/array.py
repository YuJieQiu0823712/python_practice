import array

class EasySolution(object):
    """
    A class used to represent solution.
    """
    def duplicateZeros1089(self, arr: array) -> array:
        i=0
        while i < len(arr):
            if arr[i] != 0:
                i += 1
            else:
                arr.insert(i+1, 0) # (index,value)
                arr.pop() # pop last index
                i += 2
        return arr
    # Input: [1,0,2,3,0,4,5,0]
    # Output: [1,0,0,2,3,0,0,4]
    # TC: O(n) => O(n)+O(m)+O(1) => n is length of input, m is the position we want to insert
    # SC: O(1) We did inplace modification, no extra space.

   


e = EasySolution()
solution1 = e.duplicateZeros1089([1,0,2,3,0,4,5,0]) 




print(solution1)


