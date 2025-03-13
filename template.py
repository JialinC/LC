# BFS/DFS directions
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Bisect_left a[:i] have e < x, and all e in a[i:] have e >= x

while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] < x:
        lo = mid + 1
    else:
        hi = mid

# Bisect_right a[:i] have e <= x, and all e in a[i:] have e > x.

while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] <= x:
        lo = mid + 1
    else:
        hi = mid

# Sorts indices based on the values in arr
temp = sorted(range(n), key=lambda x: arr[x])


# Rotate 90 degrees
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
