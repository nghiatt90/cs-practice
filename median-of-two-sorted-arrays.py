# https://leetcode.com/problems/median-of-two-sorted-arrays
DEBUG = False

def debug(*message, **kwargs):
    if DEBUG:
        print(*message, **kwargs)
        
def median_array(arr):
    l = len(arr)
    return arr[l//2] if l % 2 == 1 else (arr[l//2] + arr[l//2-1]) / 2

class Solution:    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int], *args, **kwargs) -> float:
        total = len(nums1) + len(nums2)
        if total == 0:
            return 0
        if not nums1:
            return median_array(nums2)
        if not nums2:
            return median_array(nums1)

        # Both arrays should have elements now
        # Swap arrays, ensure nums1 is the start of the left side
        if nums1[0] > nums2[0]:
            nums1, nums2 = nums2, nums1
        l1, l2 = len(nums1), len(nums2)
        debug(nums1)
        debug(nums2)
        
        left_len = total // 2
        
        def binary_search(l, r):
            while l < r:
                n1 = (l + r) // 2                
                n2 = left_len - n1
                debug(f'l={l}, r={r}, n1={n1}, n2={n2}')
                if n2 > l2:
                    debug(f'n2 > l2')
                    l = n1 + 1
                elif n2 < 0:
                    debug('n2 < 0')
                    r = n1
                else:
                    max_left, min_right = None, None
                    if n1 == 0:
                        max_left = nums2[n2-1]
                    elif n2 == 0:
                        max_left = nums1[n1-1]
                    else:
                        max_left = max(nums1[n1-1], nums2[n2-1])

                    if n1 == l1:
                        min_right = nums2[n2]
                    elif n2 == l2:
                        min_right = nums1[n1]
                    else:
                        min_right = min(nums1[n1], nums2[n2])

                    debug(f'max_left={max_left}, min_right={min_right}')
                    if max_left > min_right:
                        debug('max_left > min_right')
                        x = binary_search(l, n1)
                        return x if x else binary_search(n1+1, r)
                    else:
                        debug('max_left <= min_right')
                        return min_right if total % 2 == 1 else (max_left + min_right) / 2
        
        
        l, r = 0, l1+1
        return binary_search(l, r)
