def overspeed(speeds):
    f = 0
    for speed in speeds:
        if(speed < 80):
            f = 1
    if f:
        return 0
    else:
        return 1
    
def idle(values):
    return all([x == 15 for x in values])

