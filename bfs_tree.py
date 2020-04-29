from collections import defaultdict


def func(root):

    columnTable = defaultdict(list)
    queue = deque([(root,0)])

    while queue:
        node, column = queue.popleft()
        if node is not None:
            columnTable[column].append(node.val)
            queue.append((node.left, column-1))
            queue.append((node.right, column+1))

    return [columnTable[x] for x in sorted(columnTable.keys())]


def without_sort(root):

    d = defaultdict(list)
    queue = deque([(root,0)])

    maxCol, minCol = 0,0
    while queue:
        node, column = queue.popleft()


        
        if node is not None:

            maxCol = max(maxCol, column)
            minCol = min(minCol, column)

            d[column].append(node.val)
            queue.append((node.left, column-1))
            queue.append((node.right, column+1))


    return[d[x] for x in range(minCol, maxCol+1)]




#Right Side View

def rightview(self, root):
    def dfs(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

    view = []
    dfs(root, 0)
    return view