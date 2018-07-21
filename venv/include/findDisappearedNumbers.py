# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-19 上午11:13
# File     :findDisappearedNumbers.py
# Location:/Home/PycharmProjects/..

# LeetCode No.448


class Solution:
    @staticmethod
    def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0, n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1

        result =[]
        for i in range(0, n):
            if nums[i] > 0:
                result.append(i + 1)
        return result


if __name__ == '__main__':
    print(Solution.findDisappearedNumbers([1,1]))
