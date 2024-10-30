
#Duplicate Values:

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Problem: check list for duplicates
#Solution: Time and Space: O(N): Iterage through list and create set. Space = size of set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

#[1,2,3,1] true
