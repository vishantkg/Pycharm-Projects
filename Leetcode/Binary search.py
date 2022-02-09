#Binary search
# we know that the array is sorted

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (l+r)/2

        while l<=r:
            #calculate new mid value for every iteration
            mid = int((l+r)/2)


            #check if target is present in the mid
            if target == nums[mid]:
                return mid
            
            #check if target is present in the right
            elif target <nums[mid]:
                r = mid-1

            #check if target is present in the left
            else:
                l = mid+1
        return -1

a = Solution()

nums =  [-1,0,3,5,9,12]
target = 9

print(a.search(nums, target))
