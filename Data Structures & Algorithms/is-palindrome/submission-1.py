class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []

        for c in s:
            if c.isalnum():
                cleaned.append(c.lower())
        cleaned = "".join(cleaned)
        return cleaned == cleaned[::-1]
        