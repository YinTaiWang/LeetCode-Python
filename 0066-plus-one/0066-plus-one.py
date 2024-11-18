class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        while 10 in digits:
            i = digits.index(10)
            if i == 0:
                digits[i] = 0
                digits.insert(0, 1)
            else:
                digits[i] = 0
                digits[i-1] += 1
        return digits