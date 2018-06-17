# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-17 下午12:45
# File     :intersect.py
# Location:/Home/PycharmProjects/..

# LeeCode No.350


class Solution:
    @staticmethod
    def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)
        p1 = p2 = 0
        ans = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                ans += nums1[p1],
                p1 += 1
                p2 += 1
        return ans


if __name__ == '__main__':
    print(Solution.intersect([1], [1]))
