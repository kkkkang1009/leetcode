# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        answer = []
        set1 = set(nums1)
        set2 = set(nums2)
        count1 = {}
        count2 = {}
        for i in set1:
            count1[i] = nums1.count(i)
            count2[i] = 0
        for i in set2:
            count2[i] = nums2.count(i)
        for i in set1:
            num = count1[i] if count1[i] < count2[i] else count2[i]
            answer.extend([i for j in range(num)])

        return answer