class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0
        
    def pick(self):
        return self.list[len(self.list) - 1]

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

class Tree:

    def __init__(self):
        self.Nodes = dict()

    def AddNode(self, label1, label2):
        if label1 not in self.Nodes:
            self.Nodes[label1] = Node(label1, set(), list(), None)

        if label2 not in self.Nodes:
            self.Nodes[label2] = Node(label2, set(), list(), None)

        node1 = self.Nodes[label1]
        node2 = self.Nodes[label2]

        node1.Nodes.append(node2)
        node2.Nodes.append(node1)

    def SetRoot(self, root):
        s = Stack()
        s.push(root)        

        while not s.isEmpty():
            node = s.pick()
            
            if(node.Nodes == None):
                s.pop()
                node.Count = len(node.Tag)
                if (node.Parent != None):                    
                    node.Parent.Tag = join(node.Parent.Tag, node.Tag)
                    node.Tag = None
            else:                
                for n in node.Nodes:
                    n.Nodes.remove(node)
                    n.Parent = node
                    s.push(n)
                node.Nodes = None
            

    def ColorPathFromNode(self, node, color):
        l = 0
        while node is not None and node.Visited != color:
            node.Visited = color
            node.Count = node.Count + 1
            node = node.Parent
            l = l + 1
        
    
def join(x=set(), y=set()):
    if len(x) < len(y):
        return join(y, x)
    for _ in y:
        x.add(_)
    y.clear()
    return x

class Node:

    def __init__(self, label, tag, nodes, color):
        self.Label = label
        self.Tag = tag
        self.Nodes = nodes
        self.Color = color
        self.Visited = 0
        self.Parent = None
        self.Count = 0        
       

n, m, s = input().split()
n, m, s = int(n), int(m), int(s)

t = Tree()

for i in range(0, n - 1):
    v1, v2 = input().split()
    v1, v2 = int(v1), int(v2)
    t.AddNode(v1, v2) 

for i in range(0, n):
    color = int(input())
    t.Nodes[i + 1].Tag = set([color])

t.SetRoot(t.Nodes[s])
    

for i in range(0, m):
    x = int(input())
    print(t.Nodes[x].Count)