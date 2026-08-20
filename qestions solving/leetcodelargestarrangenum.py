# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:
# Input: nums = [10,2]
# Output: "210"
# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

# better with bubble sort
class sol:
    def largestarrange(self, nums : list[int])-> str:
        n=len(nums)
        for i in range(n-1):
            swap=False
            for j in range(n-i-1):
                if str(nums[j])+str(nums[j+1])<str(nums[j+1])+str(nums[j]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swap=True
            if not swap:
                break
        result= "".join(map(str, nums))

        if result=="00":
            return 0
        return result    
obj=sol()
arr=[0,0]
print(obj.largestarrange(arr))


# but optimized here is tommorrow