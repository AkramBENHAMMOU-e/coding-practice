class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = []
        prod=1
        nbrzero = 0
        for i in nums :
            if i == 0 :
                nbrzero += 1
            else:
                prod *= i
                
        for i in range(len(nums)):
            if nbrzero > 1 :
                answers.append(0)
            elif nbrzero == 1 :
                if nums[i] == 0 :
                    answers.append(prod)
                else : 
                    answers.append(0)   
            else : 
                answers.append(prod//nums[i])

        return answers    