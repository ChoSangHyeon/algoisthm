import collections


def robber(nums:list[int]):

    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    dis = collections.OrderedDict()
    dis[0],dis[1] =nums[0], max(nums[0],nums[1])
    for i in range(2,len(nums)):
        dis[i] = max(dis[i-1],dis[i-2]+nums[i])
    return dis.popitem()[1]

print(robber([2,7,9,3,1]))

