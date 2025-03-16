### Data structure ###
# OrderedDict, can be used to implement LRU cache
d = OrderedDict.fromkeys("abcde")
d.move_to_end("b")
"".join(d)
# 'acdeb'
d.move_to_end("b", last=False)
"".join(d)
# 'bacde'

### Gereral function ###
# random generate a index in a range Example list
random.randint(0, len(l) - 1)

# BFS/DFS directions
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# keyboad
dic = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


### Binary Tree ###
# Inorder Serialization with DFS
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def ser(root, s):
            if not root:
                s += "None,"
            else:
                s += str(root.val) + ","
                s = ser(root.left, s)
                s = ser(root.right, s)
            return s

        return ser(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")[:-1]
        index = [0]

        def deser(index):
            if data[index[0]] == "None":
                index[0] += 1
                return None
            n = TreeNode(data[index[0]])
            index[0] += 1
            n.left = deser(index)
            n.right = deser(index)
            return n

        return deser(index)


### Binary Search ###
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
#  (i, j) → (j, n-1-i)
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp


# itertools
from itertools import combinations

digits = [1, 2, 3, 4]
length = 2  # Choose length of combinations
result = list(combinations(digits, length))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

from itertools import permutations

digits = [1, 2, 3, 4]
length = 2  # Choose length of permutations
result = list(permutations(digits, length))
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

from itertools import product

digits = [1, 2, 3]
length = 2
result = list(product(digits, repeat=length))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# DFS Topological Sort


# BFS Topological Sort Kahn’s Algorithm (BFS Topological Sorting) can be used to detect cycles in a directed graph.
indegree = [0] * numCourses
for i in prerequisites:
    indegree[i[0]] += 1  # Increase in-degree of course i[0]

q = deque()
for i, v in enumerate(indegree):
    if v == 0:
        q.append

ind = 0
while q:
    c = q.popleft()
    result[ind] = c
    ind += 1

    for i in prerequisites:
        if i[1] == c:
            indegree[i[0]] -= 1
            if indegree[i[0]] == 0:
                q.append(i[0])

if sum(indegree) > 0:
    return []
return result
