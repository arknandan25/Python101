# return the list with the numbers that equals the target sum

# 1st solution
def twoNumberSum(array, targetSum):
    # TC:O(n^2), SC:O(1) as no extra ds used here
    for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i], array[j]]
			
	return []

# 2nd solution
def twoNumberSum(array, targetSum):
    # TC:O(n), SC:O(n) because the values are stored in hash table
	hash_table = {}
	for num in array:
		complement = targetSum - num
		if complement in hash_table:
			return [num, complement]
		else:
			hash_table[num] = True	
	# return empty list if the condition not matched 	
	return []


# return the list with indices of the elements that equals the sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n), SC: O(n)         
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]
            else:
                hash_table[nums[i]] = i
            
            