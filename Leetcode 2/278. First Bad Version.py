class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n - 1
        result = n
        while l <= r:
            mid = (l + r) // 2;
            if isBadVersion(mid):
                result = mid;
                r = mid - 1;
            else:
                l = mid + 1;
        return result;