"""
Topological Sort Implementation
Custom implementation of topological sorting algorithm for DSA topic dependencies
"""

from typing import List, Dict, Set, Optional
from collections import defaultdict, deque

class TopologicalSort:
    """
    Topological Sort Algorithm Implementation
    
    Algorithm: Kahn's Algorithm
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)
    
    This algorithm is perfect for DSA topic dependencies because:
    1. It finds the optimal learning order
    2. It handles dependencies correctly
    3. It can detect cycles (invalid dependencies)
    4. It's efficient for our use case
    """
    
    def __init__(self, dependencies: Dict[str, List[str]]):
        """
        Initialize with topic dependencies
        
        Args:
            dependencies: Dictionary mapping topics to their prerequisites
        """
        self.dependencies = dependencies
        self.graph = self._build_adjacency_list()
        self.in_degree = self._calculate_in_degrees()
    
    def _build_adjacency_list(self) -> Dict[str, List[str]]:
        """Build adjacency list representation of the graph"""
        graph = defaultdict(list)
        
        for topic, prereqs in self.dependencies.items():
            for prereq in prereqs:
                if prereq in self.dependencies:  # Ensure prerequisite exists
                    graph[prereq].append(topic)  # prereq -> topic
        
        return dict(graph)
    
    def _calculate_in_degrees(self) -> Dict[str, int]:
        """Calculate in-degree for each node"""
        in_degree = defaultdict(int)
        
        # Initialize all topics with 0 in-degree
        for topic in self.dependencies.keys():
            in_degree[topic] = 0
        
        # Calculate in-degrees
        for topic, prereqs in self.dependencies.items():
            for prereq in prereqs:
                if prereq in self.dependencies:
                    in_degree[topic] += 1
        
        return dict(in_degree)
    
    def sort(self) -> Optional[List[str]]:
        """
        Perform topological sort using Kahn's algorithm
        
        Returns:
            Topologically sorted list of topics, or None if cycle detected
        """
        # Initialize queue with nodes having 0 in-degree
        queue = deque([topic for topic, degree in self.in_degree.items() if degree == 0])
        result = []
        in_degree_copy = self.in_degree.copy()
        
        while queue:
            current = queue.popleft()
            result.append(current)
            
            # Reduce in-degree of all neighbors
            for neighbor in self.graph.get(current, []):
                in_degree_copy[neighbor] -= 1
                if in_degree_copy[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all nodes were processed
        if len(result) == len(self.dependencies):
            return result
        else:
            # Cycle detected
            return None
    
    def sort_subgraph(self, topics: List[str]) -> Optional[List[str]]:
        """
        Perform topological sort on a subgraph
        
        Args:
            topics: List of topics to sort
            
        Returns:
            Topologically sorted list of topics, or None if cycle detected
        """
        # Create subgraph dependencies
        subgraph_deps = {}
        for topic in topics:
            if topic in self.dependencies:
                # Only include dependencies that are also in the subgraph
                subgraph_deps[topic] = [
                    dep for dep in self.dependencies[topic] 
                    if dep in topics
                ]
        
        # Create new topological sort instance for subgraph
        subgraph_sort = TopologicalSort(subgraph_deps)
        return subgraph_sort.sort()
    
    def get_learning_order(self, target_topic: str, known_topics: Optional[List[str]] = None) -> List[str]:
        """
        Get optimal learning order for a target topic
        
        Args:
            target_topic: The topic to learn
            known_topics: List of topics already known
            
        Returns:
            List of topics in optimal learning order
        """
        if known_topics is None:
            known_topics = []
        
        # Get all prerequisites for target topic
        all_prerequisites = self._get_all_prerequisites(target_topic)
        
        # Filter out known topics
        unknown_prerequisites = [topic for topic in all_prerequisites if topic not in known_topics]
        
        # Add target topic if not known
        if target_topic not in known_topics:
            unknown_prerequisites.append(target_topic)
        
        # Perform topological sort on the subgraph
        sorted_topics = self.sort_subgraph(unknown_prerequisites)
        
        if sorted_topics is None:
            # Fallback: return in dependency order
            return self._fallback_sort(unknown_prerequisites)
        
        return sorted_topics
    
    def _get_all_prerequisites(self, topic: str) -> List[str]:
        """Get all prerequisites for a topic using BFS"""
        if topic not in self.dependencies:
            return []
        
        prerequisites = set()
        visited = set()
        queue = deque([topic])
        
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            
            # Add all prerequisites
            for prereq in self.dependencies.get(current, []):
                if prereq not in visited and prereq in self.dependencies:
                    prerequisites.add(prereq)
                    queue.append(prereq)
        
        return list(prerequisites)
    
    def _fallback_sort(self, topics: List[str]) -> List[str]:
        """
        Fallback sorting when topological sort fails
        
        Args:
            topics: List of topics to sort
            
        Returns:
            Sorted list based on dependency count
        """
        # Sort by number of dependencies (fewer dependencies first)
        topic_deps = {topic: len(self.dependencies.get(topic, [])) for topic in topics}
        return sorted(topics, key=lambda x: topic_deps[x])
    
    def get_dependency_depth(self, topic: str) -> int:
        """
        Get the depth/level of a topic in the dependency graph
        
        Args:
            topic: The topic to find depth for
            
        Returns:
            Depth of the topic
        """
        if topic not in self.dependencies:
            return 0
        
        # Use dynamic programming to find maximum depth
        depth_cache = {}
        
        def calculate_depth(node: str) -> int:
            if node in depth_cache:
                return depth_cache[node]
            
            if not self.dependencies.get(node, []):
                depth_cache[node] = 0
                return 0
            
            max_depth = 0
            for prereq in self.dependencies[node]:
                if prereq in self.dependencies:
                    max_depth = max(max_depth, calculate_depth(prereq) + 1)
            
            depth_cache[node] = max_depth
            return max_depth
        
        return calculate_depth(topic)
    
    def get_topics_by_depth(self) -> Dict[int, List[str]]:
        """
        Group topics by their depth in the dependency graph
        
        Returns:
            Dictionary mapping depths to lists of topics
        """
        depths = defaultdict(list)
        
        for topic in self.dependencies.keys():
            depth = self.get_dependency_depth(topic)
            depths[depth].append(topic)
        
        return dict(depths) 