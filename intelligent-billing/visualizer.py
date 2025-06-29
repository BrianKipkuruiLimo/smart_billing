# visualizer.py

def print_tree(node, indent="", is_last=True):
    """Recursively prints the AST in a tree format"""
    if isinstance(node, (int, float, bool, str)):
        print(indent + ("└── " if is_last else "├── ") + str(node))
        return

    if isinstance(node, tuple):
        label = str(node[0])
        print(indent + ("└── " if is_last else "├── ") + label)
        indent += "    " if is_last else "│   "

        for i, child in enumerate(node[1:]):
            is_last_child = (i == len(node[1:]) - 1)
            print_tree(child, indent, is_last_child)
