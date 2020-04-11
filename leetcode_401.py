# 401. Binary Watch

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        count = 0
        for hour in range(0, 12):
            count = bin(hour)[2:].count('1')
            for minute in range(0, 60):
                if count == num:
                    result.append(str(hour)+":"+str(minute).zfill(2))
                    break
                elif count > num:
                    break
                else:
                    if count + bin(minute)[2:].count('1') == num:
                        result.append(str(hour)+":"+str(minute).zfill(2))
        return result