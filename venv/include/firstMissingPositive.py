# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-21 上午11:16
# File     :firstMissingPositive.py
# Location:/Home/PycharmProjects/..

# LeetCode No.41


class Solution:
    @staticmethod
    def firstMissingPositive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        helper = list(set(nums))
        helper.sort()
        # print(helper)
        ans = 1
        for i in helper:
            # print(i)
            if i > 0 and i == ans:
                ans += 1
            elif i > 0 and i != ans:
                return ans
        return ans


if __name__ == '__main__':
    print(Solution.firstMissingPositive([1, 1000]))
