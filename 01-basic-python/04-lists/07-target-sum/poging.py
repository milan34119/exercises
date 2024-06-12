def target_sum(xs, target):
    for i in xs:
        for j in xs:
            if i + j == target:
                return True
    return False