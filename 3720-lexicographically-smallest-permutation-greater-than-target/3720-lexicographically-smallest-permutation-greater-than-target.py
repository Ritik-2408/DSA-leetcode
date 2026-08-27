class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        n = len(s)

        best = -1
        best_char = -1

        for i in range(n):
            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    best = i
                    best_char = c
                    break

            if cnt[x] == 0:
                break

            cnt[x] -= 1

        if best == -1:
            return ""

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = target[:best]

        for ch in ans:
            cnt[ord(ch) - ord('a')] -= 1

        x = ord(target[best]) - ord('a')

        for c in range(x + 1, 26):
            if cnt[c] > 0:
                ans += chr(c + ord('a'))
                cnt[c] -= 1
                break

        for c in range(26):
            ans += chr(c + ord('a')) * cnt[c]

        return ans