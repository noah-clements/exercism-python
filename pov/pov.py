from json import dumps

# Depth first search
class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        if from_node == self.label:
            return self
        current_parent = self
        found_child = None
        for child in current_parent.children:
            try:
                if found_child := child.from_pov(from_node):
                    current_parent.children.remove(child)
                    child.children.append(current_parent)
                    return found_child
            except ValueError:
                continue
        raise ValueError("Tree could not be reoriented")

    def find_path(self, to_node):
        if self.label == to_node:
            return [to_node]
        path_list = []
        current_parent = self
        for child in current_parent.children:
            try:
                path_list = child.find_path(to_node)
            except ValueError:
                continue
        path_list.append(current_parent.label)
        if len(path_list) < 2:
            raise ValueError("No path found")
        else:
            return path_list

    def path_to(self, from_node, to_node):
        from_node_tree = self.from_pov(from_node)
        return list(reversed(from_node_tree.find_path(to_node)))

if __name__.__eq__("__main__"):
    tree = Tree("parent", [Tree("a"), Tree('y', [Tree("x")]), Tree("b"), Tree("c")])
    # print(tree)
    print(tree.from_pov("x"))
    tree = Tree("parent", [Tree("a"), Tree('y', [Tree("x")]), Tree("b"), Tree("c")])
    print(tree.path_to("x", "b"))