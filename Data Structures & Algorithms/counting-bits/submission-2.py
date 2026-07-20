class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []

        for i in range(n + 1):
            count = 0
            num = i
            while num > 0:
                if num & 1:
                    count += 1
                num >>= 1

            arr.append(count)
        return arr
