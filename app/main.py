"""
DSA Topic Recommendation System - Main Application
Streamlit web application for recommending DSA learning paths
"""

import streamlit as st
import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from data.topic_data import (
    TOPIC_DEPENDENCIES, 
    get_all_topics, 
    get_topic_description, 
    get_all_categories,
    get_topics_by_category
)
from graph.topic_graph import TopicGraph
from graph.topological_sort import TopologicalSort
from utils.helpers import (
    format_learning_path,
    create_topic_selector,
    create_multi_topic_selector,
    display_topic_info,
    create_learning_path_chart,
    display_progress,
    validate_topic_selection
)

# Page configuration
st.set_page_config(
    page_title="DSA Topic Recommendation System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': 'DSA Topic Recommendation System using Graph Algorithms'
    }
)

# Custom theme configuration
st.markdown("""
<style>
    /* Hide Streamlit's default styling */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom dark theme */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Ensure proper contrast for all text */
    .stMarkdown, .stText, .stWrite {
        color: #ffffff !important;
    }
    
    /* Fix sidebar layout issues */
    .css-1d391kg {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
        min-height: 100vh;
    }
    
    /* Ensure main content area uses full width when sidebar is collapsed */
    .main .block-container {
        max-width: 100%;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    
    /* Fix sidebar toggle button visibility */
    .css-1rs6os {
        z-index: 1000;
    }
    
    /* Ensure proper spacing */
    .stApp > div:first-child {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Import Google Fonts for better typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global font settings */
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        color: #ffffff;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5), 0 0 20px rgba(255, 255, 255, 0.3);
        letter-spacing: -0.02em;
    }
    
    .sub-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
        letter-spacing: -0.01em;
    }
    
    /* Enhanced info boxes with better contrast */
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #ffffff;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .info-box h3 {
        color: #ffffff;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    .info-box p, .info-box ul, .info-box ol {
        color: #f8f9fa;
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }
    
    .success-box {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #ffffff;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .success-box h3 {
        color: #ffffff;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    .success-box ul, .success-box ol {
        color: #f8f9fa;
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #ffffff;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .warning-box h3 {
        color: #ffffff;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    .warning-box ol {
        color: #f8f9fa;
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }
    
    /* Enhanced text styling */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    /* Better paragraph and text styling */
    p, div {
        color: #f8f9fa;
        line-height: 1.6;
    }
    
    /* Enhanced sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
    
    /* Better metric styling */
    .css-1wivap2 {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 1rem;
        backdrop-filter: blur(10px);
    }
    
    /* Enhanced button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }
    
    /* Enhanced selectbox styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: #ffffff;
    }
    
    /* Enhanced multiselect styling */
    .stMultiSelect > div > div {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: #ffffff;
    }
    
    /* Better checkbox styling */
    .stCheckbox > div > div {
        color: #ffffff;
    }
    
    /* Enhanced progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Better expander styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.1);
        color: #ffffff;
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* Enhanced error and success messages */
    .stAlert {
        border-radius: 8px;
        backdrop-filter: blur(10px);
    }
    
    /* Better table styling */
    .dataframe {
        background: rgba(255, 255, 255, 0.1);
        color: #ffffff;
        border-radius: 8px;
    }
    
    /* Enhanced plotly chart styling */
    .js-plotly-plot {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1rem;
    }
    
    /* Better list styling */
    ul, ol {
        color: #f8f9fa;
        line-height: 1.6;
    }
    
    li {
        margin-bottom: 0.5rem;
    }
    
    /* Enhanced strong and bold text */
    strong, b {
        color: #ffffff;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    /* Better link styling */
    a {
        color: #74b9ff;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: #0984e3;
        text-decoration: underline;
    }
    
    /* Enhanced code styling */
    code {
        background: rgba(255, 255, 255, 0.1);
        color: #ffffff;
        padding: 0.2rem 0.4rem;
        border-radius: 4px;
        font-family: 'Courier New', monospace;
    }
    
    /* Better blockquote styling */
    blockquote {
        background: rgba(255, 255, 255, 0.1);
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 8px;
        color: #f8f9fa;
    }
    
    /* Enhanced metric cards */
    .metric-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Better sidebar text */
    .css-1d391kg p, .css-1d391kg div {
        color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Header
    st.markdown('<h1 class="main-header">📚 DSA Topic Recommendation System</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🎯 Navigation")
        page = st.selectbox(
            "Choose a page",
            ["🏠 Home", "🔍 Topic Explorer", "📈 Learning Path", "ℹ️ About"]
        )
        
        st.markdown("---")
        st.markdown("### 💡 How it works")
        st.info("**Smart Learning Paths**\n\n"
                "• Analyzes topic dependencies\n"
                "• Finds optimal study order\n"
                "• Personalizes recommendations\n"
                "• Tracks your progress")
    
    # Initialize graph
    if 'topic_graph' not in st.session_state:
        st.session_state.topic_graph = TopicGraph(TOPIC_DEPENDENCIES)
        st.session_state.topological_sort = TopologicalSort(TOPIC_DEPENDENCIES)
    
    # Page routing
    if page == "🏠 Home":
        show_home_page()
    elif page == "🔍 Topic Explorer":
        show_topic_explorer()
    elif page == "📈 Learning Path":
        show_learning_path()
    elif page == "ℹ️ About":
        show_about_page()

def show_home_page():
    """Display the home page"""
    
    # Introduction
    st.markdown('<h2 class="sub-header">Welcome to DSA Learning Assistant!</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <h3>🎯 What is this?</h3>
        <p>This is an intelligent system that helps you find the optimal learning path for Data Structures and Algorithms topics. 
        It analyzes topic relationships and suggests the best order to study, making your learning journey more efficient and effective.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="success-box">
        <h3>✨ Key Features</h3>
        <ul>
        <li><strong>Topic Explorer:</strong> Browse all DSA topics and their dependencies</li>
        <li><strong>Learning Path Generator:</strong> Get personalized learning recommendations</li>
        <li><strong>Graph Visualization:</strong> See topic relationships visually</li>
        <li><strong>Progress Tracking:</strong> Track your learning progress</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h3>🚀 Quick Start</h3>
        <ol>
        <li>Go to <strong>Topic Explorer</strong> to browse topics</li>
        <li>Use <strong>Learning Path</strong> to get recommendations</li>
        <li>Check <strong>About</strong> to learn more</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick example
    st.markdown("---")
    st.subheader("💡 Quick Example")
    
    example_topic = "Binary Search Trees"
    example_path = st.session_state.topic_graph.get_learning_path(example_topic)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**If you want to learn:** {example_topic}")
        st.write("**The system suggests this path:**")
        for i, topic in enumerate(example_path, 1):
            st.write(f"{i}. {topic}")
    
    with col2:
        # Create a simple chart for the example
        if example_path:
            fig = create_learning_path_chart(example_path)
            st.plotly_chart(fig, use_container_width=True)

def show_topic_explorer():
    """Display the topic explorer page"""
    
    st.markdown('<h2 class="sub-header">🔍 Topic Explorer</h2>', unsafe_allow_html=True)
    
    # Category selection
    categories = get_all_categories()
    selected_category = st.selectbox("Select Category", ["All Topics"] + categories)
    
    # Get topics based on selection
    if selected_category == "All Topics":
        topics = get_all_topics()
    else:
        topics = get_topics_by_category(selected_category)
    
    # Topic selection
    selected_topic = create_topic_selector(topics, "explorer_topic", "Select a topic to explore")
    
    if selected_topic:
        st.markdown("---")
        
        # Topic information
        description = get_topic_description(selected_topic)
        dependencies = st.session_state.topic_graph.get_prerequisites(selected_topic)
        dependents = st.session_state.topic_graph.get_dependent_topics(selected_topic)
        
        col1, col2 = st.columns(2)
        
        with col1:
            display_topic_info(selected_topic, description, dependencies)
        
        with col2:
            st.subheader(f"📤 Topics that depend on {selected_topic}")
            if dependents:
                for dep in dependents:
                    st.write(f"• {dep}")
            else:
                st.write("No topics depend on this one (it's a leaf node)")
        
        # Learning path for this topic
        st.markdown("---")
        st.subheader("🎯 Learning Path to this Topic")
        
        learning_path = st.session_state.topic_graph.get_learning_path(selected_topic)
        st.markdown(format_learning_path(learning_path))
        
        # Visualize the path
        if learning_path:
            fig = create_learning_path_chart(learning_path)
            st.plotly_chart(fig, use_container_width=True)

def show_learning_path():
    """Display the learning path generator page"""
    
    st.markdown('<h2 class="sub-header">📈 Learning Path Generator</h2>', unsafe_allow_html=True)
    
    # User input section
    st.subheader("🎯 What do you want to learn?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Target topic selection
        all_topics = get_all_topics()
        target_topic = create_topic_selector(all_topics, "target_topic", "Select topic you want to learn")
    
    with col2:
        # Known topics selection
        known_topics = create_multi_topic_selector(all_topics, "known_topics", "Select topics you already know")
    
    # Generate learning path
    if target_topic and validate_topic_selection(target_topic, all_topics):
        st.markdown("---")
        
        # Get learning path
        learning_path = st.session_state.topic_graph.get_learning_path(target_topic, known_topics)
        
        # Display results
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("📚 Your Personalized Learning Path")
            st.markdown(format_learning_path(learning_path))
            
            # Learning path visualization
            if learning_path:
                fig = create_learning_path_chart(learning_path)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("📊 Path Statistics")
            
            # Calculate statistics
            total_topics = len(learning_path)
            known_in_path = len([t for t in learning_path if t in known_topics]) if known_topics else 0
            new_topics = total_topics - known_in_path
            
            st.metric("Total Topics", total_topics)
            st.metric("New Topics", new_topics)
            st.metric("Already Known", known_in_path)
            
            if total_topics > 0:
                efficiency = ((total_topics - new_topics) / total_topics) * 100
                st.metric("Path Efficiency", f"{efficiency:.1f}%")
        
        # Progress tracking
        if learning_path:
            st.markdown("---")
            st.subheader("📈 Track Your Progress")
            
            # Create progress tracker
            progress = {}
            for topic in learning_path:
                progress[topic] = st.checkbox(f"✅ Completed: {topic}", key=f"progress_{topic}")
            
            # Display progress
            display_progress(progress)

def show_about_page():
    """Display the about page"""
    
    st.markdown('<h2 class="sub-header">ℹ️ About This Project</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <h3>🎯 Project Overview</h3>
    <p>This DSA Topic Recommendation System helps students find the optimal learning path for Data Structures and Algorithms topics. 
    It analyzes topic relationships and provides personalized recommendations to make learning more efficient and effective.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧠 How it works")
        st.markdown("""
        **Smart Learning Path Generation**
        
        - **Purpose:** Find optimal learning order
        - **Method:** Analyzes topic dependencies
        - **Result:** Personalized study recommendations
        - **Benefit:** Efficient learning progression
        
        The system works by:
        1. Understanding topic relationships
        2. Identifying prerequisites
        3. Creating optimal study sequences
        4. Personalizing based on your knowledge
        5. Tracking your progress
        """)
    
    with col2:
        st.subheader("🏗️ Features & Technology")
        st.markdown("""
        **User Features:**
        - Interactive topic explorer
        - Personalized learning paths
        - Progress tracking
        - Visual dependency graphs
        
        **Technology:**
        - Python backend
        - Streamlit web interface
        - Interactive visualizations
        - Real-time recommendations
        
        **Design:**
        - Modern, responsive UI
        - Intuitive navigation
        - Beautiful visualizations
        - Mobile-friendly design
        """)
    
    st.markdown("---")
    
    st.subheader("🚀 Future Enhancements")
    st.markdown("""
    - **AI Integration:** Smart question recommendations
    - **LeetCode Integration:** Direct problem suggestions
    - **Personalized Learning:** Adaptive paths based on performance
    - **Progress Analytics:** Detailed learning analytics
    - **Mobile App:** Native mobile application
    """)

if __name__ == "__main__":
    main() 