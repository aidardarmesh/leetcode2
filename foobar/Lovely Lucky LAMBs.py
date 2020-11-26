def stingy(lambs):
    if lambs <= 1:
        return lambs
    
    n = 1
    prev, curr = 0, 1
    while True:
        lambs -= curr
        if lambs < prev + curr:
            break
        n += 1
        prev, curr = curr, prev + curr

    return n


def generous(lambs):
    n = 0
    curr = 1
    while lambs >= curr:
        n += 1
        lambs -= curr
        curr *= 2
    
    return n


def solution(total_lambs):
    return abs(generous(total_lambs) - stingy(total_lambs))

