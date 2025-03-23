### Data structure ###
# OrderedDict, can be used to implement LRU cache
d = OrderedDict.fromkeys("abcde")
d.move_to_end("b")
"".join(d)
# 'acdeb'
d.move_to_end("b", last=False)
"".join(d)
# 'bacde'

### Gereral/Common ideas ###
# random generate a index in a range Example list
random.randint(0, len(l) - 1)
# randomly select an element from a list
random.choice(l)

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

# BFS/DFS directions
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

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

# Checking for overlap between two intervals (start1, end1) and (start2, end2) 
if max(start1, start2) < min(end1, end2)

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


### Algorithms
### Binary Tree ###
# Iterative In-order Traversal
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    stk = [root]
    while stk:
        cur = stk.pop()
        res.append(cur.val)
        if cur.right:
            stk.append(cur.right)
        if cur.left:
            stk.append(cur.left)
    return res

# Iterative In-order Traversal
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    stk = []
    cur = root
    while cur or stk:
        while cur:
            stk.append(cur)
            cur = cur.left
        cur = stk.pop()
        res.append(cur.val)
        cur = cur.right
    return res

# Iterative Post-order Traversal
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    stk = [root]
    while stk:
        cur = stk.pop()
        res.append(cur.val)
        if cur.left:
            stk.append(cur.left)
        if cur.right:
            stk.append(cur.right)
    return res[::-1]

# Construct Binary Tree from Inorder and Postorder Traversal
def helper(in_left, in_right):
    # if there is no elements to construct subtrees
    if in_left > in_right:
        return None
    
    # pick up the last element as a root
    val = postorder.pop()
    root = TreeNode(val)

    # root splits inorder list
    # into left and right subtrees
    index = idx_map[val]

    # build right subtree
    root.right = helper(index + 1, in_right)
    # build left subtree
    root.left = helper(in_left, index - 1)
    return root

# Pre-order Serialization with DFS
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

### Binary Searh Tree ###
# Insert into a Binary Search Tree
def insert(root, val):
    if not root:
        return TreeNode(val)
    if root.val < val:
        root.right = insert(root.right,val)
    if root.val > val:
        root.left = insert(root.left,val)
    return root

def successor(self,node):
    node = node.right
    while node.left:
        node = node.left
    return node.val

def predecessor(self,node):
    node = node.left
    while node.right:
        node = node.right
    return node.val

def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    if not root:
        return None

    if key == root.val:
        if root.right:
            su = self.successor(root)
            root.val = su
            root.right = self.deleteNode(root.right,su)
        elif root.left:
            pr = self.predecessor(root)
            root.val = pr
            root.left = self.deleteNode(root.left,pr)
        else:
            root=None # actual deletion
    elif key > root.val:
        root.right = self.deleteNode(root.right,key)
    else:
        root.left = self.deleteNode(root.left,key)
    return root

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

### Topological Sort ###
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

### Line Sweep algorithm ###

# Divide and Conquer
def divide_and_conquer( S ):
    # (1). Divide the problem into a set of subproblems.
    [S1, S2, ... Sn] = divide(S)

    # (2). Solve the subproblem recursively,
    #   obtain the results of subproblems as [R1, R2... Rn].
    rets = [divide_and_conquer(Si) for Si in [S1, S2, ... Sn]]
    [R1, R2,... Rn] = rets

    # (3). combine the results from the subproblems.
    #   and return the combined result.
    return combine([R1, R2,... Rn])

### Sorting ###
# Merge Sort
def merge_sort(nums):
    # bottom cases: empty or list of a single element.
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums) / 2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1
    
    # append what is remained in either of the lists
    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])
    
    return ret

def quicksort(lst):
    """
    Sorts an array in the ascending order in O(n log n) time
    :param nums: a list of numbers
    :return: the sorted list
    """
    n = len(lst)
    qsort(lst, 0, n - 1)

def qsort(lst, lo, hi):
    """
    Helper
    :param lst: the list to sort
    :param lo:  the index of the first element in the list
    :param hi:  the index of the last element in the list
    :return: the sorted list
    """
    if lo < hi:
        p = partition(lst, lo, hi)
        qsort(lst, lo, p - 1)
        qsort(lst, p + 1, hi)

def partition(lst, lo, hi):
    """
    Picks the last element hi as a pivot
     and returns the index of pivot value in the sorted array
    """
    pivot = lst[hi]
    i = lo
    for j in range(lo, hi):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[hi] = lst[hi], lst[i]
    return i




