


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                continue

            if char == ')' or char == ']' or char == '}':
                if len(stack) == 0:
                    return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
                continue

            if char == ']' and stack[-1] == '[':
                stack.pop()
                continue
            if char == '}' and stack[-1] == '{':
                stack.pop()
                continue
            return False


        if len(stack)!=0:
            return False
        return True


        pass


s = "()[]{}"

sol = Solution()
# print(sol.isValid(s))
s = "(])"
print(sol.isValid(s))
