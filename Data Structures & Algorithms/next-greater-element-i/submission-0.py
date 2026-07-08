class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            e = nums1[i]
            found = False
            for j in range(len(nums2)):
                e2 = nums2[j]

                if found:
                    if e2 > e:
                        res[i] = e2
                        break
                else:
                    if e == e2:
                        found = True
        
        return res


        