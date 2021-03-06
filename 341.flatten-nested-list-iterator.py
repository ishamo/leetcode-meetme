# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.table = []

        def scan(val):
            if not val:
                return
            if isinstance(val, int):
                self.table.append(val)
            else:
                for i in val:
                    scan(i)
        scan(nestedList)

        self.iterator = 0


    def next(self):
        """
        :rtype: int
        """
        val = self.table[self.iterator]
        self.iterator += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.table) > self.iterator


# Your NestedIterator object will be instantiated and called as such:
# nestedList = [[1,1],2,[1,1]]
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# print v
