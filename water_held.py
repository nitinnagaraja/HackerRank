def water_held(heights):
    l = len(heights)
    lmax = [0] * l
    rmax = [0] * l

    total = 0
    
    for i in xrange(1, l):
        lmax[i] = max(lmax[i-1], heights[i-1]) 

    for i in xrange(l-2, -1, -1):
        rmax[i] = max(rmax[i+1], heights[i+1])
        diff = min(lmax[i], rmax[i]) - heights[i]
        if diff > 0:
            total += diff

    return total

heights = map(int, raw_input().split())
print water_held(heights)
