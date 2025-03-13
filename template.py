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
