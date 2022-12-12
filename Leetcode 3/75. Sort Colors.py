class Solution:
    def sortColors(self, A: List[int]) -> None:
        l = 0
        r = len(A) - 1
        sc = 0
        
        while sc <= r:
            if A[sc] == 0:
                A[sc], A[l] = A[l], A[sc]
                l += 1
                sc += 1
            elif A[sc] == 2:
                A[sc], A[r] = A[r], A[sc]
                r -= 1
            else:
                sc += 1
        return(A)