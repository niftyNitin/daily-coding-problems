class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def serialize(root, output):
        if not root:
            output.append("#")
            return
        output.append(root.value)
        Node.serialize(root.left, output)
        Node.serialize(root.right, output)
        return output

    @staticmethod
    def deserialize(source):
        global index
        if source[index] == "#":
            index += 1
            return None
        value = source[index]
        index += 1
        left = Node.deserialize(source)
        right = Node.deserialize(source)
        return Node(value, left, right)
