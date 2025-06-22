"""
DSA Problem Data with Links
Contains problems organized by topics and difficulty levels
Based on comprehensive LeetCode problem collection and Striver's A2Z DSA Course
"""

# Problem data structure with single links (preferring LeetCode)
PROBLEMS_DATA = {
    "Arrays": {
        "beginner": [
            {
                "title": "Two Sum",
                "description": "Find two numbers that add up to a target sum",
                "link": "https://leetcode.com/problems/two-sum/"
            },
            {
                "title": "Remove Element",
                "description": "Remove all instances of a value from array",
                "link": "https://leetcode.com/problems/remove-element/"
            },
            {
                "title": "Maximum Score After Splitting a String",
                "description": "Split string to maximize score of zeros and ones",
                "link": "https://leetcode.com/problems/maximum-score-after-splitting-a-string/"
            },
            {
                "title": "Plus One",
                "description": "Add one to a number represented as array of digits",
                "link": "https://leetcode.com/problems/plus-one/"
            },
            {
                "title": "Move Zeroes",
                "description": "Move all zeros to the end while maintaining relative order",
                "link": "https://leetcode.com/problems/move-zeroes/"
            },
            {
                "title": "Valid Mountain Array",
                "description": "Check if array is a valid mountain",
                "link": "https://leetcode.com/problems/valid-mountain-array/"
            },
            {
                "title": "Find Numbers with Even Number of Digits",
                "description": "Count numbers with even number of digits",
                "link": "https://leetcode.com/problems/find-numbers-with-even-number-of-digits/"
            },
            {
                "title": "Squares of a Sorted Array",
                "description": "Return squares of sorted array in sorted order",
                "link": "https://leetcode.com/problems/squares-of-a-sorted-array/"
            }
        ],
        "intermediate": [
            {
                "title": "3Sum",
                "description": "Find three numbers that add up to zero",
                "link": "https://leetcode.com/problems/3sum/"
            },
            {
                "title": "Container With Most Water",
                "description": "Find container that can hold the most water",
                "link": "https://leetcode.com/problems/container-with-most-water/"
            },
            {
                "title": "Set Matrix Zeroes",
                "description": "Set entire row and column to zero if element is zero",
                "link": "https://leetcode.com/problems/set-matrix-zeroes/"
            },
            {
                "title": "Spiral Matrix",
                "description": "Return elements of matrix in spiral order",
                "link": "https://leetcode.com/problems/spiral-matrix/"
            },
            {
                "title": "Rotate Image",
                "description": "Rotate matrix 90 degrees clockwise in-place",
                "link": "https://leetcode.com/problems/rotate-image/"
            },
            {
                "title": "Search a 2D Matrix II",
                "description": "Search for target in sorted 2D matrix",
                "link": "https://leetcode.com/problems/search-a-2d-matrix-ii/"
            },
            {
                "title": "Product of Array Except Self",
                "description": "Return array where each element is product of all others",
                "link": "https://leetcode.com/problems/product-of-array-except-self/"
            },
            {
                "title": "Rotate Array",
                "description": "Rotate array to the right by k steps",
                "link": "https://leetcode.com/problems/rotate-array/"
            },
            {
                "title": "Next Permutation",
                "description": "Find next lexicographically greater permutation",
                "link": "https://leetcode.com/problems/next-permutation/"
            },
            {
                "title": "Maximum Subarray",
                "description": "Find contiguous subarray with largest sum (Kadane's Algorithm)",
                "link": "https://leetcode.com/problems/maximum-subarray/"
            },
            {
                "title": "Best Time to Buy and Sell Stock",
                "description": "Find maximum profit from stock transactions",
                "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
            },
            {
                "title": "Rearrange Array Elements by Sign",
                "description": "Rearrange array alternating positive and negative",
                "link": "https://leetcode.com/problems/rearrange-array-elements-by-sign/"
            }
        ],
        "advanced": [
            {
                "title": "Median of Two Sorted Arrays",
                "description": "Find median of two sorted arrays in logarithmic time",
                "link": "https://leetcode.com/problems/median-of-two-sorted-arrays/"
            },
            {
                "title": "Trapping Rain Water",
                "description": "Calculate how much rain water can be trapped",
                "link": "https://leetcode.com/problems/trapping-rain-water/"
            },
            {
                "title": "First Missing Positive",
                "description": "Find smallest missing positive integer",
                "link": "https://leetcode.com/problems/first-missing-positive/"
            },
            {
                "title": "Max Sum of Rectangle No Larger Than K",
                "description": "Find maximum sum rectangle with sum no larger than k",
                "link": "https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/"
            },
            {
                "title": "4Sum",
                "description": "Find four numbers that add up to target",
                "link": "https://leetcode.com/problems/4sum/"
            },
            {
                "title": "Largest Rectangle in Histogram",
                "description": "Find largest rectangle area in histogram",
                "link": "https://leetcode.com/problems/largest-rectangle-in-histogram/"
            }
        ]
    },
    "Strings": {
        "beginner": [
            {
                "title": "Valid Palindrome",
                "description": "Check if a string is a palindrome",
                "link": "https://leetcode.com/problems/valid-palindrome/"
            },
            {
                "title": "Valid Anagram",
                "description": "Check if two strings are anagrams",
                "link": "https://leetcode.com/problems/valid-anagram/"
            },
            {
                "title": "Implement strStr()",
                "description": "Find first occurrence of needle in haystack",
                "link": "https://leetcode.com/problems/implement-strstr/"
            },
            {
                "title": "Length of Last Word",
                "description": "Return length of last word in string",
                "link": "https://leetcode.com/problems/length-of-last-word/"
            },
            {
                "title": "Reverse String",
                "description": "Reverse a string in-place",
                "link": "https://leetcode.com/problems/reverse-string/"
            },
            {
                "title": "First Unique Character in a String",
                "description": "Find first non-repeating character",
                "link": "https://leetcode.com/problems/first-unique-character-in-a-string/"
            }
        ],
        "intermediate": [
            {
                "title": "Longest Palindromic Substring",
                "description": "Find the longest palindromic substring",
                "link": "https://leetcode.com/problems/longest-palindromic-substring/"
            },
            {
                "title": "Group Anagrams",
                "description": "Group strings that are anagrams together",
                "link": "https://leetcode.com/problems/group-anagrams/"
            },
            {
                "title": "Longest Substring Without Repeating Characters",
                "description": "Find length of longest substring without repeating characters",
                "link": "https://leetcode.com/problems/longest-substring-without-repeating-characters/"
            },
            {
                "title": "String to Integer (atoi)",
                "description": "Convert string to integer with validation",
                "link": "https://leetcode.com/problems/string-to-integer-atoi/"
            },
            {
                "title": "Longest Common Prefix",
                "description": "Find longest common prefix among strings",
                "link": "https://leetcode.com/problems/longest-common-prefix/"
            },
            {
                "title": "Count and Say",
                "description": "Generate nth term of count-and-say sequence",
                "link": "https://leetcode.com/problems/count-and-say/"
            },
            {
                "title": "Sort Characters By Frequency",
                "description": "Sort characters by frequency in descending order",
                "link": "https://leetcode.com/problems/sort-characters-by-frequency/"
            }
        ],
        "advanced": [
            {
                "title": "Minimum Window Substring",
                "description": "Find minimum window substring containing all characters",
                "link": "https://leetcode.com/problems/minimum-window-substring/"
            },
            {
                "title": "Edit Distance",
                "description": "Minimum operations to convert one string to another",
                "link": "https://leetcode.com/problems/edit-distance/"
            },
            {
                "title": "Regular Expression Matching",
                "description": "Implement regular expression matching",
                "link": "https://leetcode.com/problems/regular-expression-matching/"
            },
            {
                "title": "Wildcard Matching",
                "description": "Implement wildcard pattern matching",
                "link": "https://leetcode.com/problems/wildcard-matching/"
            },
            {
                "title": "Palindromic Substrings",
                "description": "Count number of palindromic substrings",
                "link": "https://leetcode.com/problems/palindromic-substrings/"
            }
        ]
    },
    "Linked Lists": {
        "beginner": [
            {
                "title": "Reverse Linked List",
                "description": "Reverse a singly linked list",
                "link": "https://leetcode.com/problems/reverse-linked-list/"
            },
            {
                "title": "Merge Two Sorted Lists",
                "description": "Merge two sorted linked lists",
                "link": "https://leetcode.com/problems/merge-two-sorted-lists/"
            },
            {
                "title": "Remove Duplicates from Sorted List",
                "description": "Remove duplicates from sorted linked list",
                "link": "https://leetcode.com/problems/remove-duplicates-from-sorted-list/"
            },
            {
                "title": "Linked List Cycle",
                "description": "Detect if a linked list has a cycle",
                "link": "https://leetcode.com/problems/linked-list-cycle/"
            },
            {
                "title": "Intersection of Two Linked Lists",
                "description": "Find intersection point of two linked lists",
                "link": "https://leetcode.com/problems/intersection-of-two-linked-lists/"
            },
            {
                "title": "Palindrome Linked List",
                "description": "Check if linked list is palindrome",
                "link": "https://leetcode.com/problems/palindrome-linked-list/"
            },
            {
                "title": "Middle of the Linked List",
                "description": "Find middle node of linked list",
                "link": "https://leetcode.com/problems/middle-of-the-linked-list/"
            },
            {
                "title": "Delete Node in a Linked List",
                "description": "Delete a node without access to head",
                "link": "https://leetcode.com/problems/delete-node-in-a-linked-list/"
            }
        ],
        "intermediate": [
            {
                "title": "Add Two Numbers",
                "description": "Add two numbers represented as linked lists",
                "link": "https://leetcode.com/problems/add-two-numbers/"
            },
            {
                "title": "Remove Nth Node From End of List",
                "description": "Remove nth node from end of linked list",
                "link": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/"
            },
            {
                "title": "Swap Nodes in Pairs",
                "description": "Swap every two adjacent nodes",
                "link": "https://leetcode.com/problems/swap-nodes-in-pairs/"
            },
            {
                "title": "Rotate List",
                "description": "Rotate linked list to the right by k places",
                "link": "https://leetcode.com/problems/rotate-list/"
            },
            {
                "title": "Remove Duplicates from Sorted List II",
                "description": "Remove all duplicates from sorted linked list",
                "link": "https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/"
            },
            {
                "title": "Partition List",
                "description": "Partition list around value x",
                "link": "https://leetcode.com/problems/partition-list/"
            },
            {
                "title": "Reverse Linked List II",
                "description": "Reverse linked list from position m to n",
                "link": "https://leetcode.com/problems/reverse-linked-list-ii/"
            },
            {
                "title": "Copy List with Random Pointer",
                "description": "Deep copy linked list with random pointers",
                "link": "https://leetcode.com/problems/copy-list-with-random-pointer/"
            },
            {
                "title": "Reverse Nodes in k-Group",
                "description": "Reverse nodes in groups of k",
                "link": "https://leetcode.com/problems/reverse-nodes-in-k-group/"
            },
            {
                "title": "Odd Even Linked List",
                "description": "Group odd and even positioned nodes together",
                "link": "https://leetcode.com/problems/odd-even-linked-list/"
            }
        ],
        "advanced": [
            {
                "title": "Merge k Sorted Lists",
                "description": "Merge k sorted linked lists",
                "link": "https://leetcode.com/problems/merge-k-sorted-lists/"
            },
            {
                "title": "Linked List Cycle II",
                "description": "Find where cycle begins in linked list",
                "link": "https://leetcode.com/problems/linked-list-cycle-ii/"
            },
            {
                "title": "LRU Cache",
                "description": "Design and implement LRU cache",
                "link": "https://leetcode.com/problems/lru-cache/"
            },
            {
                "title": "Sort List",
                "description": "Sort linked list using O(n log n) time",
                "link": "https://leetcode.com/problems/sort-list/"
            },
            {
                "title": "Flatten a Multilevel Doubly Linked List",
                "description": "Flatten multilevel doubly linked list",
                "link": "https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/"
            }
        ]
    },
    "Binary Trees": {
        "beginner": [
            {
                "title": "Maximum Depth of Binary Tree",
                "description": "Find the maximum depth of a binary tree",
                "link": "https://leetcode.com/problems/maximum-depth-of-binary-tree/"
            },
            {
                "title": "Same Tree",
                "description": "Check if two binary trees are the same",
                "link": "https://leetcode.com/problems/same-tree/"
            },
            {
                "title": "Invert Binary Tree",
                "description": "Invert a binary tree",
                "link": "https://leetcode.com/problems/invert-binary-tree/"
            },
            {
                "title": "Symmetric Tree",
                "description": "Check if tree is mirror of itself",
                "link": "https://leetcode.com/problems/symmetric-tree/"
            },
            {
                "title": "Path Sum",
                "description": "Check if tree has root-to-leaf path with sum",
                "link": "https://leetcode.com/problems/path-sum/"
            },
            {
                "title": "Minimum Depth of Binary Tree",
                "description": "Find minimum depth of binary tree",
                "link": "https://leetcode.com/problems/minimum-depth-of-binary-tree/"
            },
            {
                "title": "Balanced Binary Tree",
                "description": "Check if binary tree is height-balanced",
                "link": "https://leetcode.com/problems/balanced-binary-tree/"
            },
            {
                "title": "Diameter of Binary Tree",
                "description": "Find diameter of binary tree",
                "link": "https://leetcode.com/problems/diameter-of-binary-tree/"
            }
        ],
        "intermediate": [
            {
                "title": "Binary Tree Inorder Traversal",
                "description": "Perform inorder traversal of binary tree",
                "link": "https://leetcode.com/problems/binary-tree-inorder-traversal/"
            },
            {
                "title": "Binary Tree Preorder Traversal",
                "description": "Perform preorder traversal of binary tree",
                "link": "https://leetcode.com/problems/binary-tree-preorder-traversal/"
            },
            {
                "title": "Binary Tree Postorder Traversal",
                "description": "Perform postorder traversal of binary tree",
                "link": "https://leetcode.com/problems/binary-tree-postorder-traversal/"
            },
            {
                "title": "Binary Tree Level Order Traversal",
                "description": "Level order traversal of binary tree",
                "link": "https://leetcode.com/problems/binary-tree-level-order-traversal/"
            },
            {
                "title": "Validate Binary Search Tree",
                "description": "Check if a binary tree is a valid BST",
                "link": "https://leetcode.com/problems/validate-binary-search-tree/"
            },
            {
                "title": "Convert Sorted Array to Binary Search Tree",
                "description": "Convert sorted array to height-balanced BST",
                "link": "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/"
            },
            {
                "title": "Path Sum II",
                "description": "Find all root-to-leaf paths with given sum",
                "link": "https://leetcode.com/problems/path-sum-ii/"
            },
            {
                "title": "Binary Tree Zigzag Level Order Traversal",
                "description": "Zigzag level order traversal",
                "link": "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/"
            },
            {
                "title": "Lowest Common Ancestor of a Binary Tree",
                "description": "Find LCA of two nodes in binary tree",
                "link": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/"
            }
        ],
        "advanced": [
            {
                "title": "Binary Tree Maximum Path Sum",
                "description": "Find the maximum path sum in a binary tree",
                "link": "https://leetcode.com/problems/binary-tree-maximum-path-sum/"
            },
            {
                "title": "Construct Binary Tree from Preorder and Inorder Traversal",
                "description": "Build tree from preorder and inorder traversals",
                "link": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/"
            },
            {
                "title": "Serialize and Deserialize Binary Tree",
                "description": "Serialize and deserialize binary tree",
                "link": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/"
            },
            {
                "title": "Binary Tree Right Side View",
                "description": "Return right side view of binary tree",
                "link": "https://leetcode.com/problems/binary-tree-right-side-view/"
            },
            {
                "title": "Flatten Binary Tree to Linked List",
                "description": "Flatten binary tree to linked list in-place",
                "link": "https://leetcode.com/problems/flatten-binary-tree-to-linked-list/"
            },
            {
                "title": "Morris Inorder Traversal",
                "description": "Inorder traversal with O(1) space complexity",
                "link": "https://leetcode.com/problems/binary-tree-inorder-traversal/"
            }
        ]
    },
    "Dynamic Programming": {
        "beginner": [
            {
                "title": "Climbing Stairs",
                "description": "Count ways to climb stairs",
                "link": "https://leetcode.com/problems/climbing-stairs/"
            },
            {
                "title": "Fibonacci Number",
                "description": "Calculate the nth Fibonacci number",
                "link": "https://leetcode.com/problems/fibonacci-number/"
            },
            {
                "title": "House Robber",
                "description": "Maximum money that can be robbed",
                "link": "https://leetcode.com/problems/house-robber/"
            },
            {
                "title": "Maximum Subarray",
                "description": "Find the contiguous subarray with the largest sum",
                "link": "https://leetcode.com/problems/maximum-subarray/"
            },
            {
                "title": "Min Cost Climbing Stairs",
                "description": "Find minimum cost to reach top of stairs",
                "link": "https://leetcode.com/problems/min-cost-climbing-stairs/"
            },
            {
                "title": "Pascal's Triangle",
                "description": "Generate Pascal's triangle",
                "link": "https://leetcode.com/problems/pascals-triangle/"
            }
        ],
        "intermediate": [
            {
                "title": "Coin Change",
                "description": "Find minimum coins needed for amount",
                "link": "https://leetcode.com/problems/coin-change/"
            },
            {
                "title": "Longest Increasing Subsequence",
                "description": "Find length of longest increasing subsequence",
                "link": "https://leetcode.com/problems/longest-increasing-subsequence/"
            },
            {
                "title": "House Robber II",
                "description": "House robber with circular arrangement",
                "link": "https://leetcode.com/problems/house-robber-ii/"
            },
            {
                "title": "Decode Ways",
                "description": "Count ways to decode numeric string",
                "link": "https://leetcode.com/problems/decode-ways/"
            },
            {
                "title": "Unique Paths",
                "description": "Count unique paths in grid",
                "link": "https://leetcode.com/problems/unique-paths/"
            },
            {
                "title": "Minimum Path Sum",
                "description": "Find minimum sum path in grid",
                "link": "https://leetcode.com/problems/minimum-path-sum/"
            },
            {
                "title": "Palindromic Substrings",
                "description": "Count palindromic substrings",
                "link": "https://leetcode.com/problems/palindromic-substrings/"
            },
            {
                "title": "0-1 Knapsack Problem",
                "description": "Classic 0-1 knapsack dynamic programming",
                "link": "https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/"
            },
            {
                "title": "Subset Sum Problem",
                "description": "Check if subset with given sum exists",
                "link": "https://www.geeksforgeeks.org/subset-sum-problem-dp-25/"
            }
        ],
        "advanced": [
            {
                "title": "Edit Distance",
                "description": "Minimum operations to convert one string to another",
                "link": "https://leetcode.com/problems/edit-distance/"
            },
            {
                "title": "Longest Common Subsequence",
                "description": "Find length of longest common subsequence",
                "link": "https://leetcode.com/problems/longest-common-subsequence/"
            },
            {
                "title": "Regular Expression Matching",
                "description": "Implement regular expression matching",
                "link": "https://leetcode.com/problems/regular-expression-matching/"
            },
            {
                "title": "Best Time to Buy and Sell Stock IV",
                "description": "Maximum profit with at most k transactions",
                "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/"
            },
            {
                "title": "Burst Balloons",
                "description": "Maximum coins from bursting balloons",
                "link": "https://leetcode.com/problems/burst-balloons/"
            },
            {
                "title": "Longest Palindromic Subsequence",
                "description": "Find longest palindromic subsequence",
                "link": "https://leetcode.com/problems/longest-palindromic-subsequence/"
            }
        ]
    },
    "Graphs": {
        "beginner": [
            {
                "title": "Number of Islands",
                "description": "Count number of islands in a 2D grid",
                "link": "https://leetcode.com/problems/number-of-islands/"
            },
            {
                "title": "Flood Fill",
                "description": "Perform flood fill on 2D image",
                "link": "https://leetcode.com/problems/flood-fill/"
            },
            {
                "title": "Find Center of Star Graph",
                "description": "Find center node of star graph",
                "link": "https://leetcode.com/problems/find-center-of-star-graph/"
            },
            {
                "title": "Find if Path Exists in Graph",
                "description": "Check if path exists between two nodes",
                "link": "https://leetcode.com/problems/find-if-path-exists-in-graph/"
            }
        ],
        "intermediate": [
            {
                "title": "Course Schedule",
                "description": "Check if all courses can be finished",
                "link": "https://leetcode.com/problems/course-schedule/"
            },
            {
                "title": "Clone Graph",
                "description": "Clone an undirected graph",
                "link": "https://leetcode.com/problems/clone-graph/"
            },
            {
                "title": "Pacific Atlantic Water Flow",
                "description": "Find cells where water can flow to both oceans",
                "link": "https://leetcode.com/problems/pacific-atlantic-water-flow/"
            },
            {
                "title": "Course Schedule II",
                "description": "Find order to finish all courses",
                "link": "https://leetcode.com/problems/course-schedule-ii/"
            },
            {
                "title": "Surrounded Regions",
                "description": "Capture surrounded regions on board",
                "link": "https://leetcode.com/problems/surrounded-regions/"
            },
            {
                "title": "Rotting Oranges",
                "description": "Time for all oranges to rot",
                "link": "https://leetcode.com/problems/rotting-oranges/"
            },
            {
                "title": "Detect Cycle in Undirected Graph",
                "description": "Detect cycle in undirected graph using DFS/BFS",
                "link": "https://www.geeksforgeeks.org/detect-cycle-undirected-graph/"
            }
        ],
        "advanced": [
            {
                "title": "Word Ladder",
                "description": "Find shortest transformation sequence",
                "link": "https://leetcode.com/problems/word-ladder/"
            },
            {
                "title": "Alien Dictionary",
                "description": "Find order of characters in alien language",
                "link": "https://leetcode.com/problems/alien-dictionary/"
            },
            {
                "title": "Network Delay Time",
                "description": "Find time for signal to reach all nodes",
                "link": "https://leetcode.com/problems/network-delay-time/"
            },
            {
                "title": "Critical Connections in a Network",
                "description": "Find bridges in graph",
                "link": "https://leetcode.com/problems/critical-connections-in-a-network/"
            },
            {
                "title": "Shortest Path in Binary Matrix",
                "description": "Find shortest path in binary matrix",
                "link": "https://leetcode.com/problems/shortest-path-in-binary-matrix/"
            }
        ]
    },
    "Binary Search": {
        "beginner": [
            {
                "title": "Binary Search",
                "description": "Implement binary search algorithm",
                "link": "https://leetcode.com/problems/binary-search/"
            },
            {
                "title": "Search Insert Position",
                "description": "Find position to insert target in sorted array",
                "link": "https://leetcode.com/problems/search-insert-position/"
            },
            {
                "title": "First Bad Version",
                "description": "Find first bad version using API",
                "link": "https://leetcode.com/problems/first-bad-version/"
            },
            {
                "title": "Sqrt(x)",
                "description": "Compute square root of x",
                "link": "https://leetcode.com/problems/sqrtx/"
            },
            {
                "title": "Guess Number Higher or Lower",
                "description": "Guess number using binary search",
                "link": "https://leetcode.com/problems/guess-number-higher-or-lower/"
            }
        ],
        "intermediate": [
            {
                "title": "Search in Rotated Sorted Array",
                "description": "Search element in rotated sorted array",
                "link": "https://leetcode.com/problems/search-in-rotated-sorted-array/"
            },
            {
                "title": "Find Peak Element",
                "description": "Find peak element in array",
                "link": "https://leetcode.com/problems/find-peak-element/"
            },
            {
                "title": "Search a 2D Matrix",
                "description": "Search target in 2D matrix",
                "link": "https://leetcode.com/problems/search-a-2d-matrix/"
            },
            {
                "title": "Find First and Last Position of Element",
                "description": "Find first and last position in sorted array",
                "link": "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"
            },
            {
                "title": "Search in Rotated Sorted Array II",
                "description": "Search in rotated array with duplicates",
                "link": "https://leetcode.com/problems/search-in-rotated-sorted-array-ii/"
            }
        ],
        "advanced": [
            {
                "title": "Find Minimum in Rotated Sorted Array",
                "description": "Find minimum element in rotated sorted array",
                "link": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"
            },
            {
                "title": "Median of Two Sorted Arrays",
                "description": "Find median of two sorted arrays",
                "link": "https://leetcode.com/problems/median-of-two-sorted-arrays/"
            },
            {
                "title": "Kth Smallest Element in a Sorted Matrix",
                "description": "Find kth smallest element in sorted matrix",
                "link": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/"
            },
            {
                "title": "Aggressive Cows",
                "description": "Place cows with maximum minimum distance",
                "link": "https://www.geeksforgeeks.org/aggressive-cows-problem/"
            },
            {
                "title": "Allocate Minimum Number of Pages",
                "description": "Allocate books to minimize maximum pages",
                "link": "https://www.geeksforgeeks.org/allocate-minimum-number-pages/"
            }
        ]
    },
    "Backtracking": {
        "beginner": [
            {
                "title": "Generate Parentheses",
                "description": "Generate all combinations of well-formed parentheses",
                "link": "https://leetcode.com/problems/generate-parentheses/"
            },
            {
                "title": "Letter Combinations of a Phone Number",
                "description": "Generate letter combinations from phone number",
                "link": "https://leetcode.com/problems/letter-combinations-of-a-phone-number/"
            },
            {
                "title": "Binary Watch",
                "description": "Find all possible times on binary watch",
                "link": "https://leetcode.com/problems/binary-watch/"
            }
        ],
        "intermediate": [
            {
                "title": "Permutations",
                "description": "Generate all permutations of array",
                "link": "https://leetcode.com/problems/permutations/"
            },
            {
                "title": "Subsets",
                "description": "Generate all possible subsets",
                "link": "https://leetcode.com/problems/subsets/"
            },
            {
                "title": "Combination Sum",
                "description": "Find combinations that sum to target",
                "link": "https://leetcode.com/problems/combination-sum/"
            },
            {
                "title": "Word Search",
                "description": "Search for word in 2D board",
                "link": "https://leetcode.com/problems/word-search/"
            },
            {
                "title": "Palindrome Partitioning",
                "description": "Partition string into palindromes",
                "link": "https://leetcode.com/problems/palindrome-partitioning/"
            },
            {
                "title": "Combination Sum II",
                "description": "Find unique combinations that sum to target",
                "link": "https://leetcode.com/problems/combination-sum-ii/"
            }
        ],
        "advanced": [
            {
                "title": "N-Queens",
                "description": "Solve the N-Queens puzzle",
                "link": "https://leetcode.com/problems/n-queens/"
            },
            {
                "title": "Sudoku Solver",
                "description": "Solve sudoku puzzle",
                "link": "https://leetcode.com/problems/sudoku-solver/"
            },
            {
                "title": "Word Search II",
                "description": "Find all words from dictionary in board",
                "link": "https://leetcode.com/problems/word-search-ii/"
            },
            {
                "title": "Rat in a Maze",
                "description": "Find path for rat to reach destination",
                "link": "https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/"
            },
            {
                "title": "M-Coloring Problem",
                "description": "Color graph with m colors",
                "link": "https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/"
            }
        ]
    },
    "Stacks": {
        "beginner": [
            {
                "title": "Valid Parentheses",
                "description": "Check if parentheses are valid",
                "link": "https://leetcode.com/problems/valid-parentheses/"
            },
            {
                "title": "Implement Queue using Stacks",
                "description": "Implement queue using stack operations",
                "link": "https://leetcode.com/problems/implement-queue-using-stacks/"
            },
            {
                "title": "Remove All Adjacent Duplicates In String",
                "description": "Remove adjacent duplicates using stack",
                "link": "https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/"
            },
            {
                "title": "Baseball Game",
                "description": "Calculate baseball game score using stack",
                "link": "https://leetcode.com/problems/baseball-game/"
            }
        ],
        "intermediate": [
            {
                "title": "Min Stack",
                "description": "Design stack with min operation",
                "link": "https://leetcode.com/problems/min-stack/"
            },
            {
                "title": "Evaluate Reverse Polish Notation",
                "description": "Evaluate expression in reverse polish notation",
                "link": "https://leetcode.com/problems/evaluate-reverse-polish-notation/"
            },
            {
                "title": "Daily Temperatures",
                "description": "Find next warmer temperature for each day",
                "link": "https://leetcode.com/problems/daily-temperatures/"
            },
            {
                "title": "Next Greater Element I",
                "description": "Find next greater element using stack",
                "link": "https://leetcode.com/problems/next-greater-element-i/"
            },
            {
                "title": "Next Greater Element II",
                "description": "Next greater in circular array",
                "link": "https://leetcode.com/problems/next-greater-element-ii/"
            },
            {
                "title": "Asteroid Collision",
                "description": "Simulate asteroid collisions",
                "link": "https://leetcode.com/problems/asteroid-collision/"
            }
        ],
        "advanced": [
            {
                "title": "Largest Rectangle in Histogram",
                "description": "Find largest rectangle area in histogram",
                "link": "https://leetcode.com/problems/largest-rectangle-in-histogram/"
            },
            {
                "title": "Trapping Rain Water",
                "description": "Calculate trapped rain water",
                "link": "https://leetcode.com/problems/trapping-rain-water/"
            },
            {
                "title": "Maximal Rectangle",
                "description": "Find largest rectangle in binary matrix",
                "link": "https://leetcode.com/problems/maximal-rectangle/"
            },
            {
                "title": "Sum of Subarray Minimums",
                "description": "Sum of minimum of all subarrays",
                "link": "https://leetcode.com/problems/sum-of-subarray-minimums/"
            }
        ]
    },
    "Heaps": {
        "beginner": [
            {
                "title": "Kth Largest Element in an Array",
                "description": "Find kth largest element using heap",
                "link": "https://leetcode.com/problems/kth-largest-element-in-an-array/"
            },
            {
                "title": "Last Stone Weight",
                "description": "Simulate stone smashing game",
                "link": "https://leetcode.com/problems/last-stone-weight/"
            },
            {
                "title": "K Closest Points to Origin",
                "description": "Find k closest points using heap",
                "link": "https://leetcode.com/problems/k-closest-points-to-origin/"
            }
        ],
        "intermediate": [
            {
                "title": "Top K Frequent Elements",
                "description": "Find k most frequent elements",
                "link": "https://leetcode.com/problems/top-k-frequent-elements/"
            },
            {
                "title": "Merge k Sorted Lists",
                "description": "Merge k sorted linked lists using heap",
                "link": "https://leetcode.com/problems/merge-k-sorted-lists/"
            },
            {
                "title": "Find Median from Data Stream",
                "description": "Find median using two heaps",
                "link": "https://leetcode.com/problems/find-median-from-data-stream/"
            },
            {
                "title": "Kth Smallest Element in a Sorted Matrix",
                "description": "Find kth smallest using heap",
                "link": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/"
            }
        ],
        "advanced": [
            {
                "title": "Sliding Window Maximum",
                "description": "Maximum in sliding window using heap",
                "link": "https://leetcode.com/problems/sliding-window-maximum/"
            },
            {
                "title": "IPO",
                "description": "Maximize capital using heaps",
                "link": "https://leetcode.com/problems/ipo/"
            },
            {
                "title": "Smallest Range Covering Elements from K Lists",
                "description": "Find smallest range using heap",
                "link": "https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/"
            }
        ]
    }
}

def get_problems_by_topic_and_level(topic: str, level: str = "all"):
    """
    Get problems filtered by topic and difficulty level
    
    Args:
        topic: DSA topic name
        level: Difficulty level (beginner, intermediate, advanced, all)
    
    Returns:
        List of problems matching the criteria
    """
    if topic not in PROBLEMS_DATA:
        return []
    
    topic_problems = PROBLEMS_DATA[topic]
    
    if level == "all":
        all_problems = []
        for diff_level in ["beginner", "intermediate", "advanced"]:
            if diff_level in topic_problems:
                problems_with_level = []
                for problem in topic_problems[diff_level]:
                    problem_copy = problem.copy()
                    problem_copy["level"] = diff_level
                    problems_with_level.append(problem_copy)
                all_problems.extend(problems_with_level)
        return all_problems
    
    if level in topic_problems:
        problems_with_level = []
        for problem in topic_problems[level]:
            problem_copy = problem.copy()
            problem_copy["level"] = level
            problems_with_level.append(problem_copy)
        return problems_with_level
    
    return []

def get_available_topics_for_problems():
    """Get all topics that have problems available"""
    return list(PROBLEMS_DATA.keys())

def get_difficulty_levels():
    """Get all available difficulty levels"""
    return ["beginner", "intermediate", "advanced", "all"]

def get_problem_count_by_topic():
    """Get count of problems for each topic"""
    counts = {}
    for topic, levels in PROBLEMS_DATA.items():
        total_count = 0
        for level, problems in levels.items():
            total_count += len(problems)
        counts[topic] = total_count
    return counts 