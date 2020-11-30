from collections import deque


def solution(x, y):
    x, y = int(x), int(y)
    gen = 0

    while min(x,y) != 1:
        if max(x,y) % min(x,y) == 0:
            return 'impossible'
        
        gen += max(x,y) / min(x,y)
        x,y = max(x,y) % min(x,y), min(x,y)
    
    return str(gen + max(x,y) - 1)


if __name__ == '__main__':
    assert solution('4', '7') == '4'
    assert solution('2', '1') == '1'
    assert solution('2', '4') == 'impossible'
