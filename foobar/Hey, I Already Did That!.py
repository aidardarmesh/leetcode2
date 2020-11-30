def solution(n, b):
    processed = {}
    cnt, k = 0, len(n)

    while True:
        if n in processed:
            return cnt - processed[n]

        processed[n] = cnt
        cnt += 1

        more, less = sorted(n, reverse=True), sorted(n)
        n = subtract(more, less, k, b)
    
    return -1


def subtract(more, less, k, b):
    res = []
    borrowed = False

    for i in range(k-1, -1, -1):
        num1, num2 = int(more[i]), int(less[i])

        if borrowed:
            num1 -= 1
        
        if num1 < num2:
            num1 += b
            borrowed = True
        else:
            borrowed = False
        
        res.append(str(num1-num2))
    
    return ''.join(res[::-1])


if __name__  == '__main__':
    assert subtract('211110', '011112', 6, 3) == '122221'
    assert subtract('222211', '112222', 6, 3) == '102212'
    assert subtract('222110', '011222', 6, 3) == '210111'

    assert solution('210022', 3) == 3
    assert solution('1211', 10) == 1
