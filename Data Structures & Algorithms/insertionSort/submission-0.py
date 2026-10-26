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
            k = j - 1
            while k >= 0 and pairs[k].key > pairs[j].key:
                temp = pairs[k]
                pairs[k] = pairs[j]
                pairs[j] = temp
                k -= 1
                j -= 1
            state.append(pairs[:])
        
        return state

        