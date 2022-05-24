

def shannon_fano(probs, beg, end):
    if(beg == end): return
    y = beg
    z = end
    sumLeft = 0.0
    sumRight = 0.0
    while(y<=z):
        if(sumLeft<=sumRight):
            sumLeft += probs[y][0]
            y += 1
        else:
            sumRight+=probs[z][0]
            z -= 1
    for h in range(beg, y):
        probs[h][1][1] =  probs[h][1][1] + "1"
    for h in range(y, end + 1):
        probs[h][1][1] =  probs[h][1][1] + "0"
    
    sf(probs, beg, y-1)
    sf(probs, y, end)
