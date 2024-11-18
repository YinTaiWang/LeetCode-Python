class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_list = [i for i in str(x)]
            if x_list != x_list[::-1]:
                return False
            return True