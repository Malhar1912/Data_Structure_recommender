def generate_explanation(structure, context):
    base_expl = {
        "stack": "Stacks use LIFO. Useful for backtracking, recursive calls, or parsing nested expressions.",
        "queue": "Queues follow FIFO. Best for fair scheduling, BFS traversal, or real-time processing.",
        "heap": "Heaps implement priority queues, ideal for greedy problems and dynamically maintaining min/max.",
        "hash table": "Hash tables support fast lookup. Useful for caching, duplicate checks, and key-value storage.",
        "graph": "Graphs represent networks. Suitable for shortest path, connected components, or topology.",
        "tree": "Trees model hierarchies and recursion, ideal for search (BST), parse trees, etc.",
        "trie": "Tries manage prefixes efficiently. Useful in dictionary problems, autocomplete, and pattern search."
    }
    fsm_note = f"FSM-style reasoning: state transitions are driven by operations implied in problem (e.g., LIFO for stack)."
    return f"🔹 Why {structure.title()}?\n{base_expl.get(structure)}\n\n🔸 FSM-style Insight:\n{fsm_note}\n\n🧠 Contextual Clues: {context}"