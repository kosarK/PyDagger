class Node:
    def __init__(self, label, val=None):
        self.__val = val
        self.__label = label
        self.next = []
        self.previous = []

    def set_val(self, val):
        self.__val = val

    def set_label(self, ver_label):
        self.__label = ver_label

    def get_val(self):
        return self.__val

    def get_label(self):
        return self.__label


class Dag:

    def __init__(self):
        self.nodes = []
        # also set?
        # self.head = None
    # @staticmethod
    def find_path(self, visited: list, src_node, dest_node):
        stack = []
        stack.append(src_node)
        while len(stack):
            s = stack[-1]
            stack.pop()
            if s not in visited:
                if s is dest_node:
                    return True
                visited.append(s)
            for node in s.next:
                if node not in visited:
                    stack.append(node)
        return False

    def add_node(self, node):
        self.nodes.append(node)
        return node

    def del_node(self, node, force_del=False):
        if node in self.nodes:
            if not force_del:
                if len(node.previous) != 0:
                    return "dependency error"
                    # throw exception?
            else:
                if len(node.next) != 0:
                    for adjacent in node.next:
                        adjacent.previous.remove(node)
                if len(node.previous) != 0:
                    for adjacent in node.previous:
                        adjacent.next.remove(node)
                self.nodes.remove(node)
        return "there is no such node"

    def del_edge(self, src_node, dest_node):
        if dest_node in src_node.next:
            dest_node.previous.remove(src_node)
            src_node.next.remove(dest_node)
        else:
            return "there is no such edge"

    def add_edge(self, src_node, dest_node):
        visited = []
        if not self.find_path(visited, dest_node, src_node):
            src_node.next.append(dest_node)
            dest_node.previous.append(src_node)
        print(f'visited ist : {[i.get_label() for i in visited]}')

    def next(self):
        pass

    def show(self):
        mydict={}
        for i in self.nodes:
            if len(i.next) != 0 :
                 mydict[i.get_label()] = [j.get_label() for j in i.next ]
            else:
                mydict[i.get_label()] = []
        print(mydict)
        print([i.get_label() for i in self.nodes])



f = Node("a", 2.3)
s = Node("b", 4.6)
t=Node("c", 4)
fo=Node("d",6)

d = Dag()

d.add_node(f)
d.add_node(s)
d.add_node(t)
d.add_node(fo)

d.add_edge(f, s)
d.add_edge(s,t)
d.add_edge(t,fo)
d.add_edge(fo,f)


d.show()

