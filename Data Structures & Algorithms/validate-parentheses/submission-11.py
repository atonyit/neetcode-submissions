class Solution:
    def isValid(self, s: str) -> bool:
        opening = "[{("
        stack = []

        # for c in s:
        #     if c in opening:
        #         stack.append(c)
        #     elif c == ']':
        #         if stack:
        #             top = stack.pop()
        #             if top != '[':
        #                 return False
        #         else:
        #             return False
        #     elif c == ')':
        #         if stack:
        #             top = stack.pop()
        #             if top != '(':
        #                 return False
        #         else:
        #             return False
        #     elif c == '}':
        #         if stack:
        #             top = stack.pop()
        #             if top != '{':
        #                 return False
        #         else:
        #             return False

        for c in s:
            if c in opening:
                stack.append(c)
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False

        return len(stack) == 0