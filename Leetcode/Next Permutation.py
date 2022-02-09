class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return None

        pointer = -1
        i=1
        while(i<len(nums)):
            if(nums[i]>nums[i-1]):
                pointer = i
            i+=1

        if pointer == -1:
            for i in range(int(len(nums)/2)):
                nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
            return None
        
        index = pointer                                 #index is the value which is to be swaped with pointer -1
        for i in range(pointer, len(nums)):
            if nums[i]>nums[pointer-1] and nums[i] <nums[index]:
                index = i

        nums[index],nums[pointer-1] = nums[pointer-1], nums[index]
        # m = nums[:pointer]
        n = nums[pointer:]
        n.sort(reverse=False)
        nums = nums[:pointer]+n

        return nums


a = Solution()

print(a.nextPermutation([1,3,2]))