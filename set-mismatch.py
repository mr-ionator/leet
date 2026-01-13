#Working Explained
#sort the array to arrange them in correct order(very important or the nums[i] == nums[i+1] breaks)
#run a loop on array and check for duplicates on the next element
# if found add the element to the output array(out_l)
#calculating the missing element
#add the missing element to array and return it



class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        out = []
        duplicate = 0;
        out_l = len(nums)
        for i in range(out_l - 1):
            if nums[i] == nums[i+1]:
                out.append(nums[i])
                duplicate  = nums[i]
        expected = out_l * (out_l+1) //2
        actual = sum(nums)
        missing = expected - actual + duplicate
        out.append(missing)
        return out
    
