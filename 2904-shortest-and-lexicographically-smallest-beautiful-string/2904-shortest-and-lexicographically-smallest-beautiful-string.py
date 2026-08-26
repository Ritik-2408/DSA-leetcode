class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']

        if len(ones) < k:
            return ""

        best = None
        best_len = float('inf')

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            length = right - left + 1
            if length < best_len:
                best_len = length
                best = s[left:right + 1]
            elif length == best_len:
                candidate = s[left:right + 1]
                if candidate < best:
                    best = candidate

        return best
