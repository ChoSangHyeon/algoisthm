class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # a = len(nums)
        # # if (a == 1):
        # #     return True
        # if(nums[0] == 0 and a != 1 ):
        #     return False
        # for i in range(a-1):
        #     nums[i+1] = max(nums[i]-1,nums[i+1])
        #     if nums[i+1] == 0:
        #         if i+2 == a:
        #             return True
        #         else:
        #             return False
        # return True 


        
        last_position = len(nums)-1

        for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
            if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
                last_position = i # Since we just need to reach to this new index
        return last_position == 0	

        # a = 1
        # if(len(nums) == 1):
        #     return True
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         a = 0
        #     nums[i] = nums[i] + a
        #     a += 1
        # b = list(filter(lambda x: nums[x] == 0, range(len(nums))))
        # if(not b):
        #     return True
        # d = []
        # for i in range(len(b)-1):
        #     if(b[i] + 1 != b[i+1]):
        #         d.append(b[i])
        # d.append(b[-1])
        # print(d)
        # c = 0
        # for i in d:
        #     print('nums[c:i]=',nums[c:i])
        #     print('i=',i,' c=',c)
        #     if(i+1 == len(nums)):
        #         if((max(nums[c:i]) < i-c +1) if nums[c:i] else True):
        #             print('f',i)
        #             return False
        #     else:
        #         if((max(nums[c:i]) <= i-c +1) if nums[c:i] else True):
        #             print('e',i)
        #             return False
        #     c = i +1
        # return True
        # ---------------------
        # if(len(nums) == 1):
        #     return True
        # if(nums[0] == 0):
        #     return False
        # a = list(filter(lambda x: nums[x] == 0, range(len(nums))))
        # if(not a):
        #     return True
        # a.append(None)
        # splist = []
        # st = 0
        # print("a=",a)
        # for i in range(len(a)):
        #     splist.append(nums[st:a[i]])
        #     st = a[i]+1 if a[i] else -1
        # for i in range(len(splist)):
        #     for j in range(len(splist[i])):
        #         splist[i][j] = splist[i][j] + j
        #     print(splist[i])
        #     if((max(splist[i]) if splist[i] else 1000000) <= len(splist[i])):
        #         return False
        # return True