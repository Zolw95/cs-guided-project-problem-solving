"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""
# What is UPER - 
# Understand - return the indices, whats our output? : nums (list of integers), target(int)
# Plan -
# can't sort the list because we lose the indices (index)  
# execute -  
# refcet/revise - 

# nums can be arbitrary length

#Edge cases:
# what is no combo of numbers sum up to the target ? -- we're told we can assume each input has exactly one solution
# how do we return the index and not the value
# iterate over nums list using range so that we have access to the indices

    # check if the current number + any of the rest of the numbers == target
    # use another loop to go over the rest of the numbers:
        # sum them up and compare against the target
        # if they're equal:
            # grab their indices and return them as a list [num1, num2]
nums = [3, 8, 12, 17]

def two_sum(nums, target):
# iterate over nums list using range so that we have access to the indices
    for idx1 in range(len(nums)):

    # check if the current number + any of the rest of the numbers == target
    # use another loop to go over the rest of the numbers:
        for idx2 in range(idx1 + 1, len(nums)):
        # sum them up and compare against the target
        # access list by index
            sum = nums[idx1] + nums[idx2]
        # if they're equal:
            if sum == target:
            # grab their indices and return them as a list [num1, num2]
                return [idx1, idx2]
result = two_sum([3, 8, 12, 17], 15)
print(result)