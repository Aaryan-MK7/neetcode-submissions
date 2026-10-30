class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the complete word at its terminal node

    def remove_word(self, word: str) -> None:
        """Optimizes search by removing found words from the Trie."""
        # We can implement a recursive cleanup or simply prune the terminal marker
        # To keep code clean and fast, we can just clear the word reference here.
        pass

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Step 1: Build the Trie
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node.current_char = char # optional track
                node = node.children[char]
            node.word = w  # Mark the end of a valid word
        
        ROWS, COLS = len(board), len(board[0])
        result = []
        
        # Step 2: Define Backtracking DFS
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]
            
            # If a word is formed, add to result
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Mark as found to avoid duplicates
            
            # Mark cell as visited
            board[r][c] = '#'
            
            # Explore 4 neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)
            
            # Restore cell (backtrack)
            board[r][c] = char
            
            # Optimization: Prune leaf nodes dynamically to speed up runtime
            if not curr_node.children:
                parent_node.children.pop(char)

        # Step 3: Run DFS from every cell matching a Trie root character
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)
                    
        return result
