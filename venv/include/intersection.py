# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-17 下午12:17
# File     :intersection.py
# Location:/Home/PycharmProjects/..

# LeetCode No.349


class Solution:
    @staticmethod
    def intersection(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    print(Solution.intersection([1,2,2,1], [2,2]))
