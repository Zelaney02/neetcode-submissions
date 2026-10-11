class Solution:
    def isPalindrome(self, s: str) -> bool:
        # #remove all spaces and symbols => convert
        # lower_s = "".join(char.lower() for char in s if char.isalnum())
        # # match half of it  in reverse or all
        # reverse_s = lower_s[::-1]
        # if reverse_s == lower_s:
        #     return True
        # else:
        #     return False

        # two pointer method
        # one pointer on each side, if isalnum() compare
        left = 0
        right = len(s) - 1

        while right > left:
            if not s[left].isalnum():
                left += 1

            elif not s[right].isalnum():
                right -= 1
            
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True





