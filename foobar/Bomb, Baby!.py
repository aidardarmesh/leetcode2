from collections import deque


def solution(x, y):
    x, y = int(x), int(y)
    queue = deque()
    queue.append((1, 1))
    gen = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            m, f = queue.popleft()

            if m == x and f == y:
                return str(gen)
            
            if m+f <= x:
                queue.append((m+f,f))
            
            if m+f <= y:
                queue.append((m,m+f))

        gen += 1
    
    return 'impossible'


if __name__ == '__main__':
    assert solution('4', '7') == '4'
    assert solution('2', '1') == '1'
    assert solution('2', '4') == 'impossible'
