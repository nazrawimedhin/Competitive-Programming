import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts_n_sqrt = list(map(lambda point: (point, math.sqrt(point[0] ** 2 + point[1] ** 2)), points))
        sorted_pts_n_sqrt = sorted(pts_n_sqrt, key=lambda pts: pts[1])
        closest_pts = []
        for i in range(k):
            close_point = sorted_pts_n_sqrt[i]
            closest_pts.append(close_point[0])
        return closest_pts
