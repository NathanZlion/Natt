# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def search_peak(self, mountain_arr: 'MountainArray', left: int, right: int) -> int:
        if left == right:
            return left
        
        mid = left + (right-left)//2

        if mountain_arr.get(mid) > mountain_arr.get(mid+1):
            return self.search_peak(mountain_arr, left, mid)

        return self.search_peak(mountain_arr, mid+1, right)


    def search_ascending(self, target: int, mountain_arr: 'MountainArray', left: int, right: int) -> int:
        # left: less than or equal to
        # right: greater than

        while right > left+1:
            mid = left + (right - left) //2

            if mountain_arr.get(mid) > target:
                right = mid
            else:
                left = mid
        
        if left == -1:
            return left

        return left if mountain_arr.get(left) == target else -1
    
    def search_descending(self, target: int, mountain_arr: 'MountainArray', left: int, right: int) -> int:
        # left: greater than
        # right: less than or equal to

        while right > left+1:
            mid = left + (right - left) //2

            if mountain_arr.get(mid) > target:
                left = mid
            else:
                right = mid
        
        if right == mountain_arr.length():
            return -1
        
        return right if mountain_arr.get(right) == target else -1

    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find the peak
        peak_index = self.search_peak(mountain_arr, 0, mountain_arr.length()-1)
        
        # perform 2 binary searches in both halves        
        index = -1

        # searching left half
        index = self.search_ascending(target, mountain_arr, -1, peak_index+1)

        # searching right half if not found in left
        return self.search_descending(target, mountain_arr, peak_index, mountain_arr.length()) if index == -1 else index        
        
        