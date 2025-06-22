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
from data.problem_data import (
    get_problems_by_topic_and_level,
    get_available_topics_for_problems,
    get_difficulty_levels,
    get_problem_count_by_topic
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
    validate_topic_selection,
    create_difficulty_selector,
    display_problems,
    create_problem_stats_chart,
    display_problem_summary
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

st.markdown("""
<style>
    /* --- THEME --- */
    :root {
        --bg-color: #1a1a1a;
        --surface-color: #282828;
        --border-color: #3d3d3d;
        --primary-color: #ffa500;
        --primary-hover-color: #ffc107;
        --text-color: #eff1f3;
        --text-secondary-color: #d1d5db;
        --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* --- GENERAL & DEFAULTS --- */
    /* Hide Streamlit's default elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }

    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* --- LAYOUT & THEME --- */
    .stApp {
        background-color: var(--bg-color);
        font-family: var(--font-family);
    }

    /* Main content area fix */
    .main .block-container {
        max-width: 100% !important;
        padding: 2rem 2rem 10rem;
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: var(--bg-color);
        border-right: 1px solid var(--border-color);
    }

    /* --- TYPOGRAPHY --- */
    /* General text contrast */
    .stMarkdown, .stText, .stWrite, .stSelectbox, .stMultiSelect {
        color: var(--text-color) !important;
    }
    
    p {
        color: var(--text-secondary-color);
        line-height: 1.6;
    }

    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        color: var(--text-color);
        margin-bottom: 2rem;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        letter-spacing: -0.02em;
    }
    
    .sub-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: var(--text-color);
        border-bottom: 2px solid var(--primary-color);
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        letter-spacing: -0.01em;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-color);
        font-weight: 600;
    }
    
    strong, b {
        color: var(--text-color);
        font-weight: 600;
    }

    a {
        color: var(--primary-color);
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: var(--primary-hover-color);
        text-decoration: underline;
    }

    code {
        background: rgba(255, 165, 0, 0.15);
        color: var(--primary-color);
        padding: 0.2rem 0.4rem;
        border-radius: 4px;
        font-family: 'Courier New', monospace;
    }

    /* --- CUSTOM BOXES & CARDS --- */
    .info-box, .success-box, .warning-box {
        color: var(--text-color);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid var(--primary-color);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        background-color: var(--surface-color);
    }
    .info-box { background-color: var(--surface-color); }
    .success-box { background-color: var(--surface-color); }
    .warning-box { background-color: var(--surface-color); }
    
    .info-box h3, .success-box h3, .warning-box h3 {
        color: var(--text-color);
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: none;
    }
    
    .info-box p, .info-box ul, .info-box ol,
    .success-box ul, .success-box ol,
    .warning-box ol {
        color: var(--text-secondary-color);
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }

    blockquote {
        background: var(--surface-color);
        border-left: 4px solid var(--primary-color);
        padding: 1rem;
        border-radius: 8px;
        color: var(--text-secondary-color);
    }

    /* --- WIDGETS --- */
    .stButton > button {
        background: var(--primary-color);
        color: var(--bg-color);
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 165, 0, 0.3);
        background: var(--primary-hover-color);
    }

    .stSelectbox > div > div, .stMultiSelect > div > div {
        background: var(--surface-color);
        border-radius: 8px;
        border: 1px solid var(--border-color);
        color: var(--text-color);
    }
    
    .stCheckbox > div > div { color: var(--text-color); }
    
    .stProgress > div > div > div {
        background: var(--primary-color);
    }
    
    .streamlit-expanderHeader {
        background: var(--surface-color);
        color: var(--text-color);
        border-radius: 8px;
        font-weight: 500;
        border: 1px solid var(--border-color);
    }

    .stAlert {
        border-radius: 8px;
        background-color: var(--surface-color);
    }
    
    .js-plotly-plot {
        background: var(--surface-color);
        border-radius: 12px;
        padding: 1rem;
        box-sizing: border-box;
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
            ["🏠 Home", "📚 Study Plan", "🧩 Problem Suggestions", "ℹ️ About"]
        )
        
        st.markdown("---")
        st.markdown("### 💡 How it works")
        st.info("**Smart Learning Paths**\n\n"
                "• Select your target topic\n"
                "• Mark topics you already know\n"
                "• Get personalized study path\n"
                "• Practice with curated problems\n"
                "• Track your progress")
    
    # Initialize graph
    if 'topic_graph' not in st.session_state:
        st.session_state.topic_graph = TopicGraph(TOPIC_DEPENDENCIES)
        st.session_state.topological_sort = TopologicalSort(TOPIC_DEPENDENCIES)
    
    # Page routing
    if page == "🏠 Home":
        show_home_page()
    elif page == "📚 Study Plan":
        show_study_plan()
    elif page == "ℹ️ About":
        show_about_page()
    elif page == "🧩 Problem Suggestions":
        show_problem_suggestions()

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
        <li><strong>Personalized Learning Paths:</strong> Get customized study recommendations</li>
        <li><strong>Smart Topic Selection:</strong> Choose your target and known topics</li>
        <li><strong>Problem Suggestions:</strong> Practice with curated problems by difficulty</li>
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
        <li>Go to <strong>Study Plan</strong> for learning paths</li>
        <li>Select the topic you want to learn</li>
        <li>Mark topics you already know</li>
        <li>Get your personalized study path!</li>
        <li>Practice with <strong>Problem Suggestions</strong></li>
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

def show_study_plan():
    """Display the study plan page"""
    
    st.markdown('<h2 class="sub-header">📚 Study Plan</h2>', unsafe_allow_html=True)
    
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
        st.subheader("📚 Your Personalized Learning Path")
        st.markdown(format_learning_path(learning_path))
        
        # Learning path visualization
        if learning_path:
            fig = create_learning_path_chart(learning_path)
            st.plotly_chart(fig, use_container_width=True)
        
        # Topic information section
        st.markdown("---")
        st.subheader(f"ℹ️ About {target_topic}")
        
        # Get topic details
        description = get_topic_description(target_topic)
        dependencies = st.session_state.topic_graph.get_prerequisites(target_topic)
        dependents = st.session_state.topic_graph.get_dependent_topics(target_topic)
        
        col1, col2 = st.columns(2)
        
        with col1:
            display_topic_info(target_topic, description, dependencies)
        
        with col2:
            st.subheader(f"📤 Topics that depend on {target_topic}")
            if dependents:
                for dep in dependents:
                    st.write(f"• {dep}")
            else:
                st.write("No topics depend on this one (it's a leaf node)")
        
        # Category information
        categories = get_all_categories()
        topic_category = None
        for category in categories:
            if target_topic in get_topics_by_category(category):
                topic_category = category
                break
        
        if topic_category:
            st.markdown("---")
            st.subheader("📂 Category Information")
            st.write(f"**Category:** {topic_category}")
            
            # Show other topics in the same category
            category_topics = get_topics_by_category(topic_category)
            if len(category_topics) > 1:
                st.write("**Other topics in this category:**")
                for topic in category_topics:
                    if topic != target_topic:
                        st.write(f"• {topic}")

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
        - Problem suggestions with links
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
    - **AI Integration:** Smart question recommendations based on performance
    - **More Problem Sources:** Integration with additional coding platforms
    - **Personalized Learning:** Adaptive paths based on performance
    - **Progress Analytics:** Detailed learning analytics and insights
    - **Mobile App:** Native mobile application
    - **Discussion Forums:** Community features for problem discussions
    """)

def show_problem_suggestions():
    """Display the problem suggestions page"""
    
    st.markdown('<h2 class="sub-header">🧩 Problem Suggestions</h2>', unsafe_allow_html=True)
    
    # User input section
    st.subheader("🎯 What level of problems do you want to practice?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Topic selection
        available_topics = get_available_topics_for_problems()
        topic = create_topic_selector(available_topics, "problem_topic", "Select topic")
    
    with col2:
        # Difficulty level selection
        difficulty_level = create_difficulty_selector("difficulty_level", "Select difficulty level")
    
    # Generate problem suggestions
    if topic and difficulty_level:
        st.markdown("---")
        
        # Get problems
        problems = get_problems_by_topic_and_level(topic, difficulty_level)
        
        if problems:
            # Display problem summary
            display_problem_summary(len(problems), topic, difficulty_level)
            
            # Display problems
            display_problems(problems, topic, difficulty_level)
            
            # Show practice tips
            st.markdown("---")
            st.subheader("💡 Practice Tips")
            
            if difficulty_level == "beginner":
                st.markdown("""
                <div class="info-box">
                <h3>🟢 Beginner Level Tips</h3>
                <ul>
                <li>Focus on understanding the problem statement clearly</li>
                <li>Start with brute force solutions, then optimize</li>
                <li>Practice basic data structure operations</li>
                <li>Don't worry about time complexity initially</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            elif difficulty_level == "intermediate":
                st.markdown("""
                <div class="info-box">
                <h3>🟡 Intermediate Level Tips</h3>
                <ul>
                <li>Focus on time and space complexity</li>
                <li>Learn multiple approaches to solve problems</li>
                <li>Practice pattern recognition</li>
                <li>Understand when to use specific algorithms</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            elif difficulty_level == "advanced":
                st.markdown("""
                <div class="info-box">
                <h3>🔴 Advanced Level Tips</h3>
                <ul>
                <li>Master complex algorithmic concepts</li>
                <li>Focus on optimal solutions</li>
                <li>Practice under time constraints</li>
                <li>Understand edge cases and corner cases</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            else:  # all levels
                st.markdown("""
                <div class="info-box">
                <h3>🌟 General Practice Tips</h3>
                <ul>
                <li>Start with easier problems and gradually increase difficulty</li>
                <li>Practice regularly and consistently</li>
                <li>Review and understand different solution approaches</li>
                <li>Join coding communities for discussion and help</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
        
        # Topic overview and statistics
        st.markdown("---")
        st.subheader("📊 Topic Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Topic description
            topic_description = get_topic_description(topic)
            st.markdown(f"""
            <div class="info-box">
            <h3>📖 About {topic}</h3>
            <p>{topic_description}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Problem statistics for all topics
            st.subheader("📈 Problem Statistics")
            problem_counts = get_problem_count_by_topic()
            
            if problem_counts:
                fig = create_problem_stats_chart(problem_counts)
                st.plotly_chart(fig, use_container_width=True)
        
        # Related topics
        if topic in TOPIC_DEPENDENCIES:
            dependencies = TOPIC_DEPENDENCIES[topic]
            if dependencies:
                st.markdown("---")
                st.subheader("🔗 Related Topics to Study First")
                st.write("Consider learning these topics before diving deep into the problems:")
                for dep in dependencies:
                    if dep in available_topics:
                        dep_count = len(get_problems_by_topic_and_level(dep, "all"))
                        st.write(f"• **{dep}** ({dep_count} problems available)")
                    else:
                        st.write(f"• **{dep}** (learning path available)")

if __name__ == "__main__":
    main() 