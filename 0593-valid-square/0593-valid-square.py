class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        def distance_squared(point1, point2):
            return (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
        
        distances = [
            distance_squared(p1, p2),
            distance_squared(p1, p3),
            distance_squared(p1, p4),
            distance_squared(p2, p3), distance_squared(p2, p4),
            distance_squared(p3, p4)
        ]
        unique_distances = set(distances)
        if len(unique_distances) != 2:
            return False
        side, diagonal = min(unique_distances), max(unique_distances)
        return distances.count(side) == 4 and distances.count(diagonal) == 2