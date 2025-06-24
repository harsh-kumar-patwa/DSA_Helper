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

def create_difficulty_selector(key: str, label: str = "Select Difficulty Level") -> str:
    """
    Create a difficulty level selector
    
    Args:
        key: Unique key for the selector
        label: Label for the selector
        
    Returns:
        Selected difficulty level
    """
    return st.selectbox(
        label,
        options=["all", "beginner", "intermediate", "advanced"],
        format_func=lambda x: {
            "all": "🌟 All Levels",
            "beginner": "🟢 Beginner",
            "intermediate": "🟡 Intermediate", 
            "advanced": "🔴 Advanced"
        }.get(x, x),
        key=key,
        help="Choose difficulty level for problem recommendations"
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
    
    try:
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
        
        # Enhanced layout configuration for better deployment compatibility
        fig.update_layout(
            xaxis_title="Learning Order",
            yaxis_title="Topics",
            height=max(400, len(topics) * 40),  # Dynamic height based on content
            margin=dict(l=20, r=20, t=40, b=20),  # Better margins for mobile
            font=dict(size=12),  # Consistent font size
            showlegend=False,  # Remove legend to save space
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
            plot_bgcolor='rgba(0,0,0,0)'   # Transparent plot area
        )
        
        # Make text more readable for deployment
        fig.update_traces(
            textposition='auto',
            textfont=dict(size=10, color='white')
        )
        
        return fig
        
    except Exception as e:
        st.error(f"Chart rendering error: {str(e)}")
        return None

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

def display_problems(problems: List[Dict], topic: str, level: str):
    """
    Display problems in a nicely formatted way
    
    Args:
        problems: List of problem dictionaries
        topic: Selected topic
        level: Selected difficulty level
    """
    if not problems:
        st.warning(f"No problems found for {topic} at {level} level!")
        return
    
    st.subheader(f"🎯 Problems for {topic}")
    
    # Show level filter info
    if level != "all":
        level_emoji = {
            "beginner": "🟢",
            "intermediate": "🟡", 
            "advanced": "🔴"
        }.get(level, "")
        st.info(f"Showing {level_emoji} **{level.title()}** level problems")
    else:
        st.info("Showing **All** difficulty levels")
    
    # Display problems
    for i, problem in enumerate(problems, 1):
        with st.expander(f"{i}. {problem['title']} ({problem.get('level', 'unknown').title()})"):
            st.write(f"**Description:** {problem['description']}")
            
            # Display single link
            if 'link' in problem:
                if 'leetcode.com' in problem['link']:
                    st.markdown(f"🟠 **Practice on LeetCode:** [Open Problem]({problem['link']})")
                elif 'geeksforgeeks.org' in problem['link']:
                    st.markdown(f"🟢 **Practice on GeeksforGeeks:** [Open Problem]({problem['link']})")
                else:
                    st.markdown(f"🔗 **Practice Link:** [Open Problem]({problem['link']})")

def create_problem_stats_chart(problem_counts: Dict[str, int]) -> go.Figure:
    """
    Create a chart showing problem count by topic
    
    Args:
        problem_counts: Dictionary mapping topics to problem counts
        
    Returns:
        Plotly figure object
    """
    if not problem_counts:
        return None
    
    try:
        topics = list(problem_counts.keys())
        counts = list(problem_counts.values())
        
        fig = px.bar(
            x=topics,
            y=counts,
            title='Available Problems by Topic',
            labels={'x': 'Topics', 'y': 'Number of Problems'},
            color=counts,
            color_continuous_scale='viridis'
        )
        
        # Enhanced layout for deployment compatibility
        fig.update_layout(
            xaxis_title="Topics",
            yaxis_title="Number of Problems",
            height=400,
            xaxis_tickangle=-45,
            margin=dict(l=20, r=20, t=40, b=60),  # Extra bottom margin for rotated labels
            font=dict(size=11),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        # Better text handling for long topic names
        fig.update_xaxes(
            tickmode='array',
            tickvals=list(range(len(topics))),
            ticktext=[topic[:15] + "..." if len(topic) > 15 else topic for topic in topics]
        )
        
        return fig
        
    except Exception as e:
        st.error(f"Stats chart rendering error: {str(e)}")
        return None

def display_problem_summary(total_problems: int, topic: str, level: str):
    """
    Display a summary of available problems
    
    Args:
        total_problems: Total number of problems
        topic: Selected topic
        level: Selected difficulty level
    """
    level_text = f"{level} level" if level != "all" else "all levels"
    
    st.markdown(f"""
    <div class="info-box">
    <h3>📊 Problem Summary</h3>
    <p>Found <strong>{total_problems}</strong> problems for <strong>{topic}</strong> at <strong>{level_text}</strong></p>
    </div>
    """, unsafe_allow_html=True) 