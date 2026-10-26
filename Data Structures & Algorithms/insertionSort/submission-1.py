# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        state = []
        
        for i, p in enumerate(pairs):
            if i == 0:
                state.append(pairs[:])
                continue
            
            j = i
   
            while j > 0 and pairs[j-1].key > pairs[j].key:
                temp = pairs[j-1]
                pairs[j-1] = pairs[j]
                pairs[j] = temp
                j -= 1
                
            state.append(pairs[:])
        
        return state

        