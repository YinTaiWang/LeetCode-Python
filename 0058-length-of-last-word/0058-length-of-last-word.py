class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        step = -1
        while len(s[step]) == 0:
            step -= 1
        else:
            return len(s[step])