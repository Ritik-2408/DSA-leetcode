class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        n = len(s)

        # Count characters
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Check if palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if freq[i] % 2 == 1:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Characters available for first half
        half_freq = [x // 2 for x in freq]

        half_len = n // 2
        half = [""] * half_len

        def make_palindrome():
            ans = "".join(half)

            if n % 2 == 1:
                ans += middle

            ans += "".join(reversed(half))

            return ans

        def solve(pos):

            if pos == half_len:
                candidate = make_palindrome()

                if candidate > target:
                    return candidate

                return ""

            t = ord(target[pos]) - ord('a')

            # First try to keep the same character
            if half_freq[t] > 0:

                half[pos] = chr(t + ord('a'))
                half_freq[t] -= 1

                result = solve(pos + 1)

                if result:
                    return result

                half_freq[t] += 1

            # Try a bigger character
            for c in range(t + 1, 26):

                if half_freq[c] > 0:

                    half[pos] = chr(c + ord('a'))
                    half_freq[c] -= 1

                    # Fill remaining positions with
                    # smallest possible characters
                    index = pos + 1

                    for x in range(26):
                        while half_freq[x] > 0:
                            half[index] = chr(x + ord('a'))
                            index += 1
                            half_freq[x] -= 1

                    return make_palindrome()

            return ""

        return solve(0)