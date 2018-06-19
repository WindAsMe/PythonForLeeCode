# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-19 上午11:13
# File     :findDisappearedNumbers.py
# Location:/Home/PycharmProjects/..

# LeeCode No.448


class Solution:
    @staticmethod
    def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                print(nums[i + 1], nums[i])
                for index in range(nums[i] + 1, nums[i + 1]):
                    result.append(index)
        return result


if __name__ == '__main__':
    print(Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
