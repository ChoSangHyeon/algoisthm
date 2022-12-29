
def maxProfit( p: list[int]) -> int:
    # listlen = len(prices)
    # if listlen == 1 or 0:
    #     return 0
    # delta = [0] * listlen
    # for i in range(listlen-1):
    #     delta[i] = prices[i+1] - prices[i]
    # i = 0
    # flag = 0
    # while i <= listlen:
    #     if delta[i] < 0 and flag == 0:
    #         i += 1
    #         continue
    # print(delta)

    # notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
    # for p in prices:
    #     hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
    # return max(notHold, notHold_cooldown)


    n = len(p)
    b = [0] * n
    s = [0] * n
    b[0] = -p[0]
    for i in range(1, len(p)):
        b[i] = max(b[i - 1], s[i - 2] - p[i])
        s[i] = max(s[i - 1], b[i - 1] + p[i])
    return s[-1]


    n = len(prices)
    if n <= 1: return 0
    
    # diff = [prices[i+1] - prices[i] for i in range(n-1)]
    # dp, dp_max = [0]*(n + 1), [0]*(n + 1)
    # for i in range(n-1):
    #     dp[i] = diff[i] + max(dp_max[i-3], dp[i-1])
    #     dp_max[i] = max(dp_max[i-1], dp[i])
        
    # return dp_max[-3]

    # s1[0] = -prices[0];
    # s0[0] = 0;
    # s2[0] = INT_MIN;
    # for (int i = 1; i < prices.size(); i++) {
    # 	s0[i] = max(s0[i - 1], s2[i - 1]);
    # 	s1[i] = max(s1[i - 1], s0[i - 1] - prices[i]);
    # 	s2[i] = s1[i - 1] + prices[i];
    # }
    # return max(s0[prices.size() - 1], s2[prices.size() - 1]);


print(maxProfit([2,10,1,10,15,5,3,4,9,8,12,5,18,22,5,13,19]))
# print(maxProfit([4,3,2,10,11,0,11]))