def overlapping_intervals(interval1, interval2):
    left1, right1 = interval1
    left2, right2 = interval2

    return left1 <= left2 <= right1 or left1 <= right2 <= right1