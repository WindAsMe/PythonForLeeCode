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
        temp = list(set(nums))
        print(temp)
        result = []
        for i in range(0, len(nums)):
            if i + 1 != temp[i]:
                result.append(i + 1)
        return result


if __name__ == '__main__':
    print(Solution.findDisappearedNumbers([1,1]))
