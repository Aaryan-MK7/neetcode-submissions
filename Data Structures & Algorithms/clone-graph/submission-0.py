
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':


        if not node:
            return None

        clones = {node: Node(node.val)}

        stack = [node]

        while stack:
            current = stack.pop()

            for neighbor in current.neighbors:

                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                clones[current].neighbors.append(
                    clones[neighbor]
                )

        return clones[node]
