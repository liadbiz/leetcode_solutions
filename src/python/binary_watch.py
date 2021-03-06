"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the
6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Given a non-negative integer n which represents the number of LEDs that are
currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:

+ The order of output does not matter.
+ The hour must not contain a leading zero, for example "01:00" is not valid, 
    it should be "1:00".
+ The minute must be consist of two digits and may contain a leading zero, for 
    example "10:2" is not valid, it should be "10:02".

"""

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        import itertools
        import math
        res = []
        n = num if num < 4 else 4
        for i in range(n + 1):
            hour = []
            minutes = []
            hour_com = list(itertools.combinations(range(4), i))
            for j in hour_com:
                h = 0
                for k in j:
                    h += int(math.pow(2, k))
                hour.append(h)
            minutes_com = list(itertools.combinations(range(6), num - i))
            for j in minutes_com:
                m = 0
                for k in j:
                    m += int(math.pow(2, k))
                minutes.append(m)
            res += [str(h) + ":0" + str(m) if m < 10 else str(h) + ":" + str(m) for h in hour for m in minutes]
        return res
            

if __name__ == "__main__":
    print(Solution().readBinaryWatch(1))
    print(Solution().readBinaryWatch(2))
