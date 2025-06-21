"""
DSA Topic Data and Dependencies
Contains all DSA topics and their prerequisite relationships
"""

# DSA Topics with their dependencies
TOPIC_DEPENDENCIES = {
    # Basic Data Structures
    "Arrays": [],
    "Strings": ["Arrays"],
    "Linked Lists": ["Arrays"],
    "Stacks": ["Arrays", "Linked Lists"],
    "Queues": ["Arrays", "Linked Lists"],
    "Trees": ["Linked Lists", "Recursion"],
    "Binary Trees": ["Trees"],
    "Binary Search Trees": ["Binary Trees"],
    "Heaps": ["Trees"],
    "Graphs": ["Trees", "Linked Lists"],
    
    # Algorithms
    "Recursion": ["Arrays"],
    "Sorting": ["Arrays", "Recursion"],
    "Searching": ["Arrays", "Sorting"],
    "Dynamic Programming": ["Recursion", "Arrays"],
    "Greedy Algorithms": ["Arrays", "Sorting"],
    "Backtracking": ["Recursion", "Arrays"],
    "Divide and Conquer": ["Recursion", "Arrays"],
    "Two Pointers": ["Arrays", "Linked Lists"],
    "Sliding Window": ["Arrays", "Two Pointers"],
    "Binary Search": ["Arrays", "Sorting"],
    
    # Advanced Topics
    "Trie": ["Trees", "Strings"],
    "Segment Trees": ["Trees", "Recursion"],
    "Union Find": ["Arrays", "Graphs"],
    "Topological Sort": ["Graphs", "DFS"],
    "Shortest Path": ["Graphs", "BFS"],
    "Minimum Spanning Tree": ["Graphs", "Greedy Algorithms"],
    
    # Graph Algorithms
    "BFS": ["Graphs", "Queues"],
    "DFS": ["Graphs", "Recursion"],
    "Cycle Detection": ["Graphs", "DFS"],
    "Connected Components": ["Graphs", "DFS"],
    
    # Advanced Data Structures
    "Hash Tables": ["Arrays"],
    "Sets": ["Hash Tables"],
    "Maps": ["Hash Tables"],
    "Priority Queues": ["Heaps"],
    
    # String Algorithms
    "String Matching": ["Strings", "Arrays"],
    "Regular Expressions": ["Strings"],
    
    # Math and Logic
    "Bit Manipulation": ["Arrays"],
    "Math": [],
    "Geometry": ["Math"],
}

# Topic categories for better organization
TOPIC_CATEGORIES = {
    "Basic Data Structures": ["Arrays", "Strings", "Linked Lists", "Stacks", "Queues"],
    "Tree-based Structures": ["Trees", "Binary Trees", "Binary Search Trees", "Heaps", "Trie", "Segment Trees"],
    "Graph Structures": ["Graphs", "BFS", "DFS", "Cycle Detection", "Connected Components"],
    "Advanced Data Structures": ["Hash Tables", "Sets", "Maps", "Priority Queues"],
    "Basic Algorithms": ["Recursion", "Sorting", "Searching", "Binary Search"],
    "Advanced Algorithms": ["Dynamic Programming", "Greedy Algorithms", "Backtracking", "Divide and Conquer"],
    "Array Techniques": ["Two Pointers", "Sliding Window"],
    "Graph Algorithms": ["Topological Sort", "Shortest Path", "Minimum Spanning Tree", "Union Find"],
    "String Algorithms": ["String Matching", "Regular Expressions"],
    "Mathematical": ["Bit Manipulation", "Math", "Geometry"]
}

# Topic descriptions for better understanding
TOPIC_DESCRIPTIONS = {
    "Arrays": "Fundamental data structure for storing elements in contiguous memory",
    "Strings": "Sequence of characters, often treated as arrays",
    "Linked Lists": "Linear data structure with nodes pointing to next element",
    "Stacks": "LIFO data structure for managing function calls and backtracking",
    "Queues": "FIFO data structure for managing breadth-first operations",
    "Trees": "Hierarchical data structure with parent-child relationships",
    "Binary Trees": "Tree where each node has at most two children",
    "Binary Search Trees": "Ordered binary tree for efficient searching",
    "Heaps": "Complete binary tree with heap property",
    "Graphs": "Collection of vertices connected by edges",
    "Recursion": "Function calling itself to solve smaller subproblems",
    "Sorting": "Arranging elements in specific order",
    "Searching": "Finding elements in data structures",
    "Dynamic Programming": "Solving complex problems by breaking into simpler subproblems",
    "Greedy Algorithms": "Making locally optimal choices at each step",
    "Backtracking": "Systematic search for solutions by trying different paths",
    "Divide and Conquer": "Breaking problem into smaller subproblems",
    "Two Pointers": "Using two pointers to solve array problems efficiently",
    "Sliding Window": "Maintaining a window of elements while processing arrays",
    "Binary Search": "Efficient search algorithm for sorted arrays",
    "Trie": "Tree-like data structure for storing strings",
    "Segment Trees": "Tree data structure for range queries",
    "Union Find": "Data structure for tracking connected components",
    "Topological Sort": "Linear ordering of vertices in directed acyclic graph",
    "Shortest Path": "Finding shortest path between vertices in graph",
    "Minimum Spanning Tree": "Tree connecting all vertices with minimum total weight",
    "BFS": "Breadth-first search for level-by-level traversal",
    "DFS": "Depth-first search for exploring graph structure",
    "Cycle Detection": "Detecting cycles in directed and undirected graphs",
    "Connected Components": "Finding groups of connected vertices",
    "Hash Tables": "Data structure for key-value pair storage",
    "Sets": "Collection of unique elements",
    "Maps": "Key-value pair data structure",
    "Priority Queues": "Queue with priority-based ordering",
    "String Matching": "Finding patterns within strings",
    "Regular Expressions": "Pattern matching and text processing",
    "Bit Manipulation": "Operations on individual bits",
    "Math": "Mathematical concepts and operations",
    "Geometry": "Geometric algorithms and concepts"
}

def get_all_topics():
    """Get all available topics"""
    return list(TOPIC_DEPENDENCIES.keys())

def get_topic_dependencies(topic):
    """Get dependencies for a specific topic"""
    return TOPIC_DEPENDENCIES.get(topic, [])

def get_topic_description(topic):
    """Get description for a specific topic"""
    return TOPIC_DESCRIPTIONS.get(topic, "No description available")

def get_topics_by_category(category):
    """Get topics belonging to a specific category"""
    return TOPIC_CATEGORIES.get(category, [])

def get_all_categories():
    """Get all available categories"""
    return list(TOPIC_CATEGORIES.keys()) 