# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quick(pairs, 0, len(pairs)-1)
        return pairs

    def quick(self, lst, s, e):
        if not lst:
            return None

        if s >= e:
            return lst
        
        pivot = lst[e]

        i = insertPos = s

        while i < e:
            if lst[i].key < pivot.key:
                lst[insertPos], lst[i] = lst[i], lst[insertPos]
                insertPos += 1
            i += 1

        lst[insertPos], lst[e] = lst[e], lst[insertPos]

        self.quick(lst, s, insertPos - 1)
        self.quick(lst, insertPos+1, e)



        
        