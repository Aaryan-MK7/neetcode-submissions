
class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        values = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if values[i] == "N":
                i += 1
                return None

            node = TreeNode(int(values[i]))
            i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()