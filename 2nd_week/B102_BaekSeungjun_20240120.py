class Solution(object):
    def intersection(self, nums1, nums2):
        answer = []
        for e in nums1:
            if e in nums2:
                answer.append(e)
        
        return list(set(answer))