import array

class EasySolution(object):
    """
    A class used to represent easy level solutions.
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

   
    def MergSortedArray88(self, num1: array, num2: array) -> array:
        # compare A to B 
        # if A>B => A put in C
        # else => B put in C
        # (pointer start from the last: ptr_a->num1 last / ptr_b->num2 last / ptr_c->last)
        # pointer-=1

        m = len(num1) - len(num2)
        n = len(num2)
  
        ptr_a = m-1
        ptr_b = n-1
        last = m+n-1

        while ptr_a>=0 and ptr_b>=0:
            if num1[ptr_a] > num2[ptr_b]:
                num1[last] = num1[ptr_a]
                ptr_a-=1
                last-=1
            else:
                num1[last] = num2[ptr_b]
                ptr_b-=1
                last-=1
        
        
        while ptr_b>=0:
            num1[last] = num2[ptr_b]
            ptr_b-=1
            last-=1

        return num1  
    # Input: num1=[1,2,3,0,0,0]
    #        num2=[2,5,6]
    # Output: [1,2,2,3,5,6]
    # TC: O(n) => O(m)+O(n) => m is length of num1, n is length of num2
    # SC: O(1) We did inplace modification, no extra space.




   


e = EasySolution()
sol1 = e.duplicateZeros1089([1,0,2,3,0,4,5,0]) 
sol2 = e.MergSortedArray88([1,2,3,0,0,0],[2,5,6])



print(sol1)
print(sol2)


