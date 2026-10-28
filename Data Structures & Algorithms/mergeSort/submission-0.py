# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.srt(0, len(pairs)-1, pairs)
        return pairs

    def merge(self, s, m, e, arr):
        L = arr[s:m+1]
        R = arr[m+1:e+1]
        k = s
        i = 0
        j = 0

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return arr
       

    def srt(self, s, e, arr):
        if s >= e:
            return arr

        m = (s + e) // 2

        self.srt(s, m, arr)
        self.srt(m+1, e, arr)

        return self.merge(s, m, e, arr)
