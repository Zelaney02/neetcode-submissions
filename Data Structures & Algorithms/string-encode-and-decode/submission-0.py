class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            result.append(str(len(s)) + "#" + s)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter
            while s[j] != "#":
                j += 1

            # Read the length
            length = int(s[i:j])

            # Extract exactly 'length' characters
            result.append(s[j + 1:j + 1 + length])

            # Move to the next string
            i = j + 1 + length

        return result