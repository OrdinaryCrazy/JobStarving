class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # refer: https://www.cnblogs.com/grandyang/p/4465932.html
        # O(log(min(m,n)))
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        # n1 >= n2
        n1 = len(nums1)
        n2 = len(nums2)
        if n2 == 0:
            return (nums1[(n1 - 1)//2] + nums1[n1//2]) / 2.0
        left_2, right_2 = 0, 2 * n2
        while(left_2 <= right_2):
            mid_2 = (left_2 + right_2) // 2
            mid_1 = n1 + n2 - mid_2
            # print(mid_1, mid_2)
            L1 = -float("inf") if mid_1 == 0 else nums1[(mid_1 - 1)//2]
            R1 = float("inf") if mid_1 == 2 * n1 else nums1[(mid_1)//2]
            L2 = -float("inf") if mid_2 == 0 else nums2[(mid_2 - 1)//2]
            R2 = float("inf") if mid_2 == 2 * n2 else nums2[(mid_2)//2]
            # print(L1, R1, L2, R2, left_2, right_2)
            if L1 > R2:
                left_2 = mid_2 + 1
            elif L2 > R1:
                right_2 = mid_2 - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0    
            
        return -1.0
        

# class Solution:
#     def medianOfSorted(self, nums: List[int]) -> float:
#         if len(nums) % 2 == 0:
#             return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2.0
#         else:
#             return nums[len(nums) // 2]
        
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
#         if not nums1:
#             return self.medianOfSorted(nums2)
#         if not nums2:
#             return self.medianOfSorted(nums1)
#         if nums1[0] > nums2[-1]:
#             return self.medianOfSorted(nums2 + nums1)
#         if nums1[-1] < nums2[0]:
#             return self.medianOfSorted(nums1 + nums2)
        
#         def midOf3(a, b, c):
#             return a + b + c - max(a, b, c) - min(a, b, c)
        
#         def midOf4(a, b, c, d):
#             return (a + b + c + d - max(a, b, c, d) - min(a, b, c, d)) / 2.0
        
#         if len(nums2) > len(nums1):
#             nums1, nums2 = nums2, nums1
        
#         if len(nums2) == 1:
#             if len(nums1) % 2 == 0:
#                 return midOf3(nums2[0], nums1[len(nums1) // 2 - 1], nums1[len(nums1) // 2])
#             else:
#                 if len(nums1) == 1:
#                     return (nums2[0] + nums1[0]) / 2.0
#                 else:
#                     another_mid = midOf3(nums2[0], nums1[len(nums1) // 2 - 1], nums1[len(nums1) // 2 + 1])
#                     return (nums1[len(nums1) // 2] + another_mid) / 2.0
        
#         if len(nums2) == 2:
#             if len(nums1) % 2 == 0:
#                 if len(nums1) == 2:
#                     return midOf4(nums1[0], nums1[1], nums2[0], nums2[1])
#                 else:
#                     low = max(nums2[0], nums1[len(nums1) // 2 - 2])
#                     high = min(nums2[1], nums1[len(nums1) // 2 + 1])
#                     return midOf4(nums1[len(nums1) // 2], nums1[len(nums1) // 2 - 1], low, high)
#             else:
#                 low = max(nums2[0], nums1[len(nums1) // 2 - 1])
#                 high = min(nums2[1], nums1[len(nums1) // 2 + 1])
#                 return midOf3(nums1[len(nums1) // 2], low, high)
        
#         if self.medianOfSorted(nums1) > self.medianOfSorted(nums2):
#             # print(nums1[:len(nums1)//2 + len(nums1)%2], nums2[len(nums2)//2 + len(nums2)%2:])
#             return self.findMedianSortedArrays(nums1[:len(nums1)//2 + len(nums1)%2], nums2[len(nums2)//2 + len(nums2)%2:])
#         else:
#             # print(nums1[len(nums1) // 2 + len(nums1)%2:], nums2[:len(nums2)//2 + len(nums2)%2])
#             return self.findMedianSortedArrays(nums1[len(nums1) // 2 + len(nums1)%2:], nums2[:len(nums2)//2 + len(nums2)%2])
        
        