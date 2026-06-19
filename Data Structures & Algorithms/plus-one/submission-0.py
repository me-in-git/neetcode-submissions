class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numb=0
        mul=1
        for i in range(len(digits)-1,-1,-1):
            numb+=digits[i]*mul
            mul*=10
        
        return [int(ch) for ch in str(numb + 1)]
       
       
        




        