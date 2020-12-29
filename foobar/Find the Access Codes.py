def solution(l):
    def divs(l, i):
        cnt = 0
        for j in range(i):
            if l[i] % l[j] == 0:
                cnt += 1
        return cnt

    def mlps(l, i):
        cnt = 0
        n = len(l)
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                cnt += 1
        return cnt

    res = 0
    n = len(l)
    for i in range(n):
        res += divs(l, i) * mlps(l, i)
    
    return res


if __name__ == '__main__':
    assert solution([1,1,1]) == 1
    assert solution([1,2,3,4,5,6]) == 3
