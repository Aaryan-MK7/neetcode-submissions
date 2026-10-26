class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):
            
            count[s[right]] = count.get(s[right], 0) + 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length