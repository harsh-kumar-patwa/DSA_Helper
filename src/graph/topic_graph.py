"""
Topic Graph Implementation
Manages DSA topic dependencies and provides graph operations
"""

import networkx as nx
from typing import List, Dict, Set, Optional
from collections import defaultdict, deque

class TopicGraph:
    def __init__(self, topic_dependencies: Dict[str, List[str]]):
        """
        Initialize the topic graph with dependencies
        
        Args:
            topic_dependencies: Dictionary mapping topics to their prerequisites
        """
        self.topic_dependencies = topic_dependencies
        self.graph = self._build_graph()
        
    def _build_graph(self) -> nx.DiGraph:
        """Build NetworkX directed graph from topic dependencies"""
        G = nx.DiGraph()
        
        # Add all topics as nodes
        for topic in self.topic_dependencies.keys():
            G.add_node(topic)
        
        # Add edges (dependencies)
        for topic, dependencies in self.topic_dependencies.items():
            for dep in dependencies:
                if dep in self.topic_dependencies:  # Ensure dependency exists
                    G.add_edge(dep, topic)  # dep -> topic (dep is prerequisite)
        
        return G
    
    def get_prerequisites(self, topic: str) -> List[str]:
        """
        Get all prerequisites for a given topic
        
        Args:
            topic: The topic to find prerequisites for
            
        Returns:
            List of prerequisite topics
        """
        if topic not in self.graph:
            return []
        
        # Use BFS to find all reachable nodes (prerequisites)
        prerequisites = set()
        visited = set()
        queue = deque([topic])
        
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            
            # Add all predecessors (prerequisites)
            for pred in self.graph.predecessors(current):
                if pred not in visited:
                    prerequisites.add(pred)
                    queue.append(pred)
        
        return list(prerequisites)
    
    def get_learning_path(self, target_topic: str, known_topics: Optional[List[str]] = None) -> List[str]:
        """
        Get optimal learning path to a target topic
        
        Args:
            target_topic: The topic to learn
            known_topics: List of topics already known (optional)
            
        Returns:
            List of topics in optimal learning order
        """
        if known_topics is None:
            known_topics = []
        
        # Get all prerequisites for the target topic
        all_prerequisites = self.get_prerequisites(target_topic)
        
        # Also get all prerequisites for known topics to avoid suggesting them
        known_prerequisites = set()
        for known_topic in known_topics:
            known_prerequisites.update(self.get_prerequisites(known_topic))
        
        # Filter out already known topics and their prerequisites
        unknown_prerequisites = [
            topic for topic in all_prerequisites 
            if topic not in known_topics and topic not in known_prerequisites
        ]
        
        # Add target topic if not known
        if target_topic not in known_topics:
            unknown_prerequisites.append(target_topic)
        
        # Perform topological sort on the subgraph
        return self._topological_sort_subgraph(unknown_prerequisites)
    
    def _topological_sort_subgraph(self, topics: List[str]) -> List[str]:
        """
        Perform topological sort on a subgraph of topics
        
        Args:
            topics: List of topics to sort
            
        Returns:
            Topologically sorted list of topics
        """
        # Create subgraph with only the specified topics
        subgraph = self.graph.subgraph(topics).copy()
        
        try:
            # Perform topological sort
            sorted_topics = list(nx.topological_sort(subgraph))
            return sorted_topics
        except nx.NetworkXError:
            # If there's a cycle, return topics in dependency order
            return self._fallback_sort(topics)
    
    def _fallback_sort(self, topics: List[str]) -> List[str]:
        """
        Fallback sorting when topological sort fails (due to cycles)
        
        Args:
            topics: List of topics to sort
            
        Returns:
            Sorted list of topics
        """
        # Simple dependency-based sorting
        topic_deps = {topic: len(self.get_prerequisites(topic)) for topic in topics}
        return sorted(topics, key=lambda x: topic_deps[x])
    
    def get_dependent_topics(self, topic: str) -> List[str]:
        """
        Get topics that depend on the given topic
        
        Args:
            topic: The prerequisite topic
            
        Returns:
            List of topics that depend on the given topic
        """
        if topic not in self.graph:
            return []
        
        dependents = set()
        visited = set()
        queue = deque([topic])
        
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            
            # Add all successors (dependent topics)
            for succ in self.graph.successors(current):
                if succ not in visited:
                    dependents.add(succ)
                    queue.append(succ)
        
        return list(dependents)
    
    def get_topic_level(self, topic: str) -> int:
        """
        Get the level/depth of a topic in the dependency graph
        
        Args:
            topic: The topic to find level for
            
        Returns:
            Level of the topic (0 for no dependencies, higher for more dependencies)
        """
        if topic not in self.graph:
            return 0
        
        # Level is the length of the longest path from any root node
        roots = [node for node in self.graph.nodes() if self.graph.in_degree(node) == 0]
        
        if not roots:
            return 0
        
        max_level = 0
        for root in roots:
            try:
                path_length = len(nx.shortest_path(self.graph, root, topic)) - 1
                max_level = max(max_level, path_length)
            except nx.NetworkXNoPath:
                continue
        
        return max_level 