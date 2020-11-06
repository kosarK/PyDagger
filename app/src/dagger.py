class Node:
    def __init__(self, label, val=None):
        self.__val = val
        self.__label = label
        self.next = None
        self.previous = None

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

    # @staticmethod
    def __findpath(self, visited: list, src_node, dest_node):
        if src_node.next is None or dest_node.previous is None: return False
        stack = [src_node]
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

    def __delete_normal_node(self, node):
        if node.next is not None :
            temp_next=node.next.copy()
            for adj in temp_next:
                self.del_edge(node, adj)
        return True

    def del_node(self, node, force_del=False):
        def delete_previous(node,force_del):
             if force_del:
                temp_pr = node.previous.copy()
                for pr_node in temp_pr:
                    self.del_edge(pr_node, node)

        def delete_next(node):
            temp_next = node.next.copy()
            for nxt_node in temp_next:
                self.del_edge(node, nxt_node)


        if node.previous is not None:
            delete_previous(node,force_del)
        if node.next is not None:
            delete_next(node)
        self.nodes.remove(node)

    def del_edge(self, src_node, dest_node):
        if src_node.next is None or dest_node not in src_node.next:
            return False
        else:
            dest_node.previous.remove(src_node)
            if len(dest_node.previous) == 0: dest_node.previous = None
            src_node.next.remove(dest_node)
            if len(src_node.next) == 0: src_node.next = None
            return True

    def add_edge(self, src_node, dest_node):
        if src_node.next is None: src_node.next = []
        if dest_node.previous is None: dest_node.previous = []
        visited = []
        if not self.__findpath(visited, dest_node, src_node):
            src_node.next.append(dest_node)
            dest_node.previous.append(src_node)

    def __next__(self):

        pass

    def show(self):
        mydict = {}
        mydict2 = {}
        for i in self.nodes:
            if i.next is not None:
                mydict[i.get_label()] = [j.get_label() for j in i.next]
            else:
                mydict[i.get_label()] = []
        print(f' node -> next : {mydict}')

        for i in self.nodes:
            if i.previous is not None:
                mydict2[i.get_label()] = [j.get_label() for j in i.previous]
            else:
                mydict2[i.get_label()] = []
        print(f' node -> previous : {mydict2}')


if __name__=='__main__':
    a = Node("a", 2.3)
    b = Node("b", 4.6)
    c = Node("c", 4)
    d = Node("d", 6)
    e = Node("e", 6)
    dag = Dag()

    dag.add_node(a)
    dag.add_node(b)
    dag.add_node(c)
    dag.add_node(d)
    dag.add_node(e)

    dag.add_edge(a, b)

    dag.add_edge(c, b)
    dag.add_edge(e, a)
    # dag.add_edge(c,a)
    # dag.add_edge(e,a)
    # dag.add_edge(d,c)
    dag.del_node(a,True)
    dag.show()
