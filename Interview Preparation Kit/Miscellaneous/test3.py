
def solution(R):
    N = len(R)
    M = len(R[0])

    # Generate grid
    grid = {}
    for i in range(N):
        for j in range(M):
            if A[i][j] == 'X':
                grid[(i, j)] = 'X'
            else:
                grid[(i, j)] = 0
    #  (0, 0) always visited
    grid[(0, 0)] = 1

    right = True
    down = False
    left = False
    up = False

    i = 0; j = 0
    # Reconsider break case
    count = 0
    while count < 1000:
        turned = False
        if right and not turned:
            if j == M-1 or grid[(i, j+1)] == 'X':
                right = False
                down = True
                turned = True
            else:
                j += 1

            grid[(i, j)] += 1
            count += 1

        if down and not turned:
            if i == N-1 or grid[(i+1, j)] == 'X':
                down = False
                left = True
                turned = True
            else:
                i += 1

            grid[(i, j)] += 1
            count += 1

        if left and not turned:
            if j == 0 or grid[(i, j-1)] == 'X':
                left = False
                up = True
                turned = True
            else:
                j -= 1

            grid[(i, j)] += 1
            count += 1

        if up and not turned:
            if i == 0 or grid[(i-1, j)] == 'X':
                up = False
                right = True
                turned = True
            else:
                i -= 1

            grid[(i, j)] += 1
            count += 1

    sum = 0
    for v in grid.values():
        if v != 0 and v != 'X':
            sum += 1

    return sum


if __name__ == '__main__':
    A = ['....X...', '........', '........', '..X.....', '........',
         '........', '.X......'] # Answer: 22
    print(solution(A))