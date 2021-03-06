# coding: utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        # i, j, k
        # i - 第几天, j - 是买还是卖, k - 可不可以买

        MP = [[0 for i in range(len(prices))] for j in range(2)]
        MP[0][0] = 0
        MP[0][1] = -prices[0]

        for i in range(1, len(prices)):
            MP[i][0] = max(MP[i-1][0], MP[i-1][1]+prices[i])
            MP[i][1] = max(MP[i-1][0]-prices[i], MP[i-1][1])


# 在第i天时，我们可以进行两种操作，抛出或是买入或是啥都不干。但是具体下来，又有四种情况：
#
# 在持有一只股票的时候抛出
# 在持有一只股票的时候啥都不干
# 在持有0只股票的时候啥都不干
# 在持有0只股票的时候买入
# 而在这些操作之间又存在潜在的联系，也就是说我如果在第i天进行以上四种操作之一，那么意味着我在第i-1天一定进行了这四种操作中的某一种，从而支持我第i天的操作。具体关联如下：
#
# 第i天执行的操作：在持有一只股票的时候抛出 => 在第i-1天执行的操作： 在持有一只股票的时候啥都不干/在持有0只股票的时候买入
# 第i天执行的操作：在持有一只股票的时候啥也不干 => 在第i-1天执行的操作：在持有一只股票的时候啥也不干/在持有0只股票的会后买入
# 第i天执行的操作：在持有0只股票的时候买入 => 在第i-1天执行的操作：在持有0只股票的时候啥也不做
# 第i天执行的操作：在持有0只股票的时候啥也不做 => 在第i-1天执行的操作：在持有0只股票的时候啥也不做/在持有一只股票的时候抛出
