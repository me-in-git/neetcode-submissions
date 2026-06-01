class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod=1
        # zero=0
        # for i in nums:
        #     if i!=0:
        #         prod*=i
        #     elif i==0:
        #         zero+=1
        

        # if zero>1:
        #     return [0]*len(nums)

        # output=[]
        # if zero==1:
        #     for i in nums:
        #         if i==0:
        #             output.append(prod)
        #         else:
        #             output.append(0)
                    
        # if zero==0:
        #     for i in nums:
        #         output.append(int(prod/i))

        pref=[1]
        post=[1]*len(nums)
        for i in range(1,len(nums)):
            pref.append(pref[i-1]*nums[i-1])
        

        for i in range(len(nums)-2,-1,-1):
            post[i]=nums[i+1]*post[i+1]

        output= [pref[i]*post[i] for i in range(len(nums))]
        return output
        