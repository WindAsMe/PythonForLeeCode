# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-6-27 上午11:51
# File     :distributeCandies.py
# Location:/Home/PycharmProjects/..

# LeeCode No.575


class Solution:
    @staticmethod
    def distribute_candies(candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(candies) == 0 or len(candies) % 2 == 1:
            return 0
        length = len(candies)
        length_set = len(set(candies))
        if length_set > length / 2:
            return int(length / 2)
        else:
            return int(length_set)


if __name__ == '__main__':
    print(Solution.distribute_candies([1,1,2,3,4,4]))