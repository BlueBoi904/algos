# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps.

# In how many distinct ways can you climb to the top?


# Number of ways to reach Step i = Number of ways to reach Step (i-1) + Number of ways to reach Step (i-2).
def climbStairs(n):
    def helper(n, memo={}):
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n not in memo:
            memo[n] = climbStairs(n - 1) + climbStairs(n - 2)
        return memo[n]
    return helper(n)
