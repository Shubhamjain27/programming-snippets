from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict()

    def add_edge(self, u,v):
        self.graph[u].append(v)



class TreeNode(object):

    """Definition of a binary tree node"""
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):

    def serialize(self, root):


        def stringify(root, string):

            if root is None:
                string += 'None'

            else:
                string += root.val
                string += stringify(root.left, string)
                string += stringify(root.right, string)

            return string

        return stringify(root, '')



    def deserialize(self, string):
        

        def maketree(string):
            if string[0] == None:
                string.pop(0)
                return None
            
            root = TreeNode(string[0])
            string.pop(0)
            root.left = maketree(string)
            root.right = maketree(string)
            return root

        data_list = data.split(',')
        root = maketree(string)
        return root