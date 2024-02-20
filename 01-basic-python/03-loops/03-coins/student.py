# Write your code here
def coins(one, two, five, goal):
    for i in range(one + 1):
        for j in range(two + 1):
            for k in range(five + 1):
                if i + 2*j + 5*k == goal:
                    return True
    return False