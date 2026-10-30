class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return None
        self.quickSort(points, 0, len(points)-1)
        return points[:k]

    def quickSort(self, points, s, e):
        if s >= e:
            return

        i = insertPos = s
        pivotPos = e
        distance_pivot = (points[pivotPos][0] - 0) ** 2 + (points[pivotPos][1] - 0) ** 2

        while i < e:
            distance_i = (points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2

            if distance_i < distance_pivot:
                points[insertPos], points[i] = points[i], points[insertPos]
                insertPos += 1
            i += 1
        
        points[pivotPos], points[insertPos] = points[insertPos], points[pivotPos] 

        self.quickSort(points, s, insertPos-1)
        self.quickSort(points, insertPos+1, e)