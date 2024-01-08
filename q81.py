class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = l + (r - l) // 2
            if nums[middle] == target: return True

            if nums[middle] == nums[l] and nums[l] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[middle]:
                if nums[l] <= target and target < nums[middle]: r = middle - 1
                else: l = middle + 1
            else:
                if nums[middle] < target and target <= nums[r]: l = middle + 1
                else: r = middle - 1
        
        return False
