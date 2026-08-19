class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = {}

        for r, s in reservedSeats:
            if r not in seats:
                seats[r] = set()
            seats[r].add(s)

        ans = (n - len(seats)) * 2

        for reserved in seats.values():
            count = 0

            if not any(s in reserved for s in range(2, 6)):
                count += 1

            if not any(s in reserved for s in range(6, 10)):
                count += 1

            if count == 0 and not any(s in reserved for s in range(4, 8)):
                count = 1

            ans += count

        return ans