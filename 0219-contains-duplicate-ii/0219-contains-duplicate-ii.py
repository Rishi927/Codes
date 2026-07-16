class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastseen={}
        for i in range(len(nums)):
            if nums[i] in lastseen and i- lastseen[nums[i]]<=k:
                return True
            lastseen[nums[i]]=i
        return False