# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 1
        e = n

        while s <= e:
            mid = (s+e) // 2
            guess_result = guess(mid)

            if guess_result == -1:
                e = mid - 1
            elif guess_result == 1:
                s = mid + 1
            else:
                return mid


        