class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '[', '{']
        closes = [')', ']', '}']
        stack = []
        if s[0] in closes:
            return False

        for i in range(len(s)):
            if (len(stack) == 0) and s[i] in closes:
                return False

            if s[i] in opens:
                stack.append(s[i])
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                print('c 3')
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True

