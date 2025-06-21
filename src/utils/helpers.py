"""
Utility Helper Functions
Common utility functions used throughout the application
"""

import streamlit as st
from typing import List, Dict, Any
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
import pandas as pd

def format_learning_path(topics: List[str]) -> str:
    """
    Format a learning path into a readable string
    
    Args:
        topics: List of topics in learning order
        
    Returns:
        Formatted string representation
    """
    if not topics:
        return "No topics to learn!"
    
    formatted = "📚 **Learning Path:**\n\n"
    for i, topic in enumerate(topics, 1):
        formatted += f"{i}. **{topic}**\n"
    
    return formatted

def create_topic_selector(topics: List[str], key: str, label: str = "Select Topic") -> str:
    """
    Create a Streamlit topic selector
    
    Args:
        topics: List of available topics
        key: Unique key for the selector
        label: Label for the selector
        
    Returns:
        Selected topic
    """
    return st.selectbox(
        label,
        options=topics,
        key=key,
        help="Choose a topic to get learning recommendations"
    )

def create_multi_topic_selector(topics: List[str], key: str, label: str = "Select Topics") -> List[str]:
    """
    Create a Streamlit multi-topic selector
    
    Args:
        topics: List of available topics
        key: Unique key for the selector
        label: Label for the selector
        
    Returns:
        List of selected topics
    """
    return st.multiselect(
        label,
        options=topics,
        key=key,
        help="Select topics you already know"
    )

def display_topic_info(topic: str, description: str, dependencies: List[str]):
    """
    Display topic information in a nice format
    
    Args:
        topic: Topic name
        description: Topic description
        dependencies: List of dependencies
    """
    st.subheader(f"📖 {topic}")
    st.write(f"**Description:** {description}")
    
    if dependencies:
        st.write("**Prerequisites:**")
        for dep in dependencies:
            st.write(f"• {dep}")
    else:
        st.write("**Prerequisites:** None (Good starting point!)")

def create_learning_path_chart(topics: List[str]) -> go.Figure:
    """
    Create a horizontal bar chart showing learning path
    
    Args:
        topics: List of topics in learning order
        
    Returns:
        Plotly figure object
    """
    if not topics:
        return None
    
    # Create data for the chart
    df = pd.DataFrame({
        'Topic': topics,
        'Order': range(1, len(topics) + 1),
        'Step': [f"Step {i}" for i in range(1, len(topics) + 1)]
    })
    
    fig = px.bar(
        df,
        x='Order',
        y='Topic',
        orientation='h',
        title='Learning Path Visualization',
        labels={'Order': 'Learning Order', 'Topic': 'Topics'},
        color='Order',
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(
        xaxis_title="Learning Order",
        yaxis_title="Topics",
        height=400
    )
    
    return fig

def create_progress_tracker(topics: List[str], completed_topics: List[str] = None) -> Dict[str, bool]:
    """
    Create a progress tracker for learning path
    
    Args:
        topics: List of topics in learning path
        completed_topics: List of completed topics
        
    Returns:
        Dictionary mapping topics to completion status
    """
    if completed_topics is None:
        completed_topics = []
    
    progress = {}
    for topic in topics:
        progress[topic] = topic in completed_topics
    
    return progress

def display_progress(progress: Dict[str, bool]):
    """
    Display learning progress
    
    Args:
        progress: Dictionary mapping topics to completion status
    """
    st.subheader("📈 Learning Progress")
    
    total = len(progress)
    completed = sum(progress.values())
    percentage = (completed / total * 100) if total > 0 else 0
    
    st.progress(percentage / 100)
    st.write(f"**Progress:** {completed}/{total} topics completed ({percentage:.1f}%)")
    
    # Show individual topic status
    for topic, is_completed in progress.items():
        status = "✅" if is_completed else "⏳"
        st.write(f"{status} {topic}")

def validate_topic_selection(selected_topic: str, available_topics: List[str]) -> bool:
    """
    Validate if selected topic is available
    
    Args:
        selected_topic: Selected topic
        available_topics: List of available topics
        
    Returns:
        True if valid, False otherwise
    """
    if not selected_topic:
        st.error("Please select a topic!")
        return False
    
    if selected_topic not in available_topics:
        st.error(f"Topic '{selected_topic}' not found in available topics!")
        return False
    
    return True 