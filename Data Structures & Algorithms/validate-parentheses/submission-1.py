class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['(', '{', '[']
        closeBrackets = [')', '}', ']']

        bracketMap = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for i in range(len(s)):
            if s[i] in openBrackets:
                stack.append(s[i])
            else:

                if len(stack) == 0:
                    return False
                
                lastBracket = stack.pop()
                if s[i] != bracketMap[lastBracket]:
                    return False

        return len(stack) == 0

