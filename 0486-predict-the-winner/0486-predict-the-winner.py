from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def max_score(l,r):
            if l == r:
                return nums[l]
            else:
                return max(nums[l]-max_score(l+1,r),nums[r]-max_score(l,r-1))


        return max_score(0,len(nums)-1) >= 0

        # rounds = len(nums) // 2 + len(nums) % 2
        # remain = len(nums)
        # dp = [[0] * len(nums) for _ in range(len(nums))]
        # lb = 0
        # rb = len(nums)-1
        # final = []
        # def makeMove(player,lb,rb,dp):
        #     dp[lb][rb] = max(dp[lb-1][rb]+nums[lb-1] * player,dp[lb][rb+1]+nums[rb+1] * player)
        #     if lb == rb:
        #         final.append(dp[lb][rb]+player * nums[lb])
        #     makeMove(player*-1,lb+1,rb,dp)
        #     makeMove(player*-1,lb,rb-1,dp)
        
        # makeMove(1,0,len(nums)-2,dp)
        # makeMove(1,1,len(nums)-1,dp)
        
        # return max(final) > 0


        # layer = len(nums) // 2 
        # mem = [0] * (2 ** layer)
        # step = 0
        # # a_t = 0
        # # b_t = 0
        # # remain = nums[max():min(n,n-a_t,b_t)]
        # accu_score = 0
        # def cal_score(a_move,b_move,remain,accu_score,men,men_loc,step):
        #     if len(remain) <= 1:
        #         accu_score += sum(remain)
        #         men[men_loc] = accu_score
        #         return
        #     else:
        #         if a_move * b_move > 0:
        #             a_score = remain[a_move]
        #             b_score = remain[a_move + b_move]
        #             if a_move > 0:
        #                 remain = remain[2:]
        #             else:
        #                 remain = remain[:-2]
        #         else:
        #             a_score = remain[a_move]
        #             b_score = remain[b_move]
        #             remain = remain[1:-1]
        #         accu_score = accu_score + a_score - b_score
            
        #         for i in [1,-1]:
        #             for j in [1,-1]:
        #                 # step += 1
        #                 cal_score(i,j,remain,accu_score,men,(i+1)//2*(2**(layer-step-1))+(j+1)//2*(2**(layer-step-2)),step+2)
        
        # for i in [1,-1]:
        #     for j in [1,-1]:
        #         # step += 1
        #         cal_score(i,j,nums,accu_score,men,(i+1)//2*(2**(layer-step-1))+(j+1)//2*(2**(layer-step-2)),step+2)