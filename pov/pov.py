from json import dumps


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
        # Depth first search
        for child in current_parent.children:
            try:
                found_child = child.from_pov(from_node)
            except ValueError:
                continue
            if found_child:
                current_parent.children.remove(found_child)
                found_child.children.append(current_parent)
                return found_child
        raise ValueError("Tree could not be reoriented")

    def path_to(self, from_node, to_node):
        pass

if __name__.__eq__("__main__"):
    tree = Tree("parent", [Tree("a"), Tree("x"), Tree("b"), Tree("c")])
    # print(tree)
    print(tree.from_pov("x"))
    # print(tree.path_to("x", "b"))