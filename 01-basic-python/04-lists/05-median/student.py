# Write your code here
def median(ns):
    sorted_list = sorted(ns)
    i = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        return (sorted_list[i-1] + sorted_list[i]) / 2
    else:
        return sorted_list[i]