class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all spaces and symbols => convert
        lower_s = "".join(char.lower() for char in s if char.isalnum())
        # match half of it  in reverse or all
        reverse_s = lower_s[::-1]
        if reverse_s == lower_s:
            return True
        else:
            return False
