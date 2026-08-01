class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = [1] + nums + [1]
        n = len(a)

        dp = [[0] * n for _ in range(n)]

        # length = distance between left and right
        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k]
                        + dp[k][right]
                        + a[left] * a[k] * a[right]
                    )

        return dp[0][n - 1]