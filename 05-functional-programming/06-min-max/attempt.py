# Write a function `closest(points, target_point)`.

# * `points`: a list of points.
# * `target_point`: a point.

# The function should return the point from `points` that is closest to `target_point`.
# In case of a tie, return the point that occurs first in the list.

# Points are represented by pairs `(x, y)`.
# The distance between two points `(x1, y1)` and `(x2, y2)` equals `((x2-x1)**2 + (y2-y1)**2)**0.5`.

def closest(points, target_point):
    def distance(point):
        x, y = point
        dx = x - tx
        dy = y - ty
        return dx**2 + dy**2
    tx, ty = target_point
    return min(points, key=distance)