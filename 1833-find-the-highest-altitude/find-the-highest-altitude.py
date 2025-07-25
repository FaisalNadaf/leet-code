class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a=[0]
        sum=0

        for i in gain:
            sum+=i
            a.append(sum)
        a.sort()

        return a[-1]