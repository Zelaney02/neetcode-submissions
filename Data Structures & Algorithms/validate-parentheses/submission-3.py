class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', '}' : '{', ']' : '['}
        for b in s:
            if b in pairs.values(): # open b
                stack.append(b)
            elif b in pairs.keys():
                if not stack or stack[-1] != pairs[b]:
                    return False
                stack.pop()
            else:
                return False
        return not stack


                