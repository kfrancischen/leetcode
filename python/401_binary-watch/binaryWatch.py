class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.number = [1,2,4,8,16,32, 100, 200, 400, 800]
        result = []
        self.backTracking(result, num, 0, 0, 0)
        return result

    def backTracking(self, result, num, path, n, start):
        if n == num:
            hour = path / 100
            minute = path % 100
            if hour > 11 or minute > 59:
                return
            time = str(hour) + ':'
            time += str(minute) if minute >= 10 else '0' + str(minute)
            result.append(time)
            return

        for i in range(start, len(self.number)):
            self.backTracking(result, num, path + self.number[i], n + 1, i + 1)


mytest = Solution()
num = 2
print mytest.readBinaryWatch(num)
