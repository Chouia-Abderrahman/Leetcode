import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if not s:
            return True
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True


sol = Solution()

print(sol.isPalindrome(' '))
print(sol.isPalindrome('A man, a plan, a canal: Panama'))
print("-------")
print(sol.isPalindrome('race a car'))
