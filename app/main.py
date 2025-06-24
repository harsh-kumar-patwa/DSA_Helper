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
from utils.gemini_chat import create_gemini_chat_interface, display_chat_interface

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
    /* --- THEME WITH FALLBACKS --- */
    :root {
        --bg-color: #1a1a1a;
        --surface-color: #282828;
        --border-color: #3d3d3d;
        --primary-color: #ffa500;
        --primary-hover-color: #ffc107;
        --text-color: #eff1f3;
        --text-secondary-color: #d1d5db;
        --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }

    /* --- GENERAL & DEFAULTS --- */
    /* Hide Streamlit's default elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }

    /* Import Google Fonts with fallback handling */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* --- LAYOUT & THEME WITH FALLBACKS --- */
    .stApp {
        background-color: var(--bg-color, #1a1a1a);
        font-family: var(--font-family, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif);
        color: var(--text-color, #eff1f3);
    }

    /* Main content area fix */
    .main .block-container {
        max-width: 100% !important;
        padding: 1rem 1rem 5rem !important;
    }
    
    /* Mobile responsive adjustments */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 0.5rem 0.5rem 3rem !important;
        }
        
        .main-header {
            font-size: 2.5rem !important;
        }
        
        .sub-header {
            font-size: 1.5rem !important;
        }
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: var(--bg-color, #1a1a1a);
        border-right: 1px solid var(--border-color, #3d3d3d);
    }

    /* --- TYPOGRAPHY WITH FALLBACKS --- */
    /* General text contrast */
    .stMarkdown, .stText, .stWrite, .stSelectbox, .stMultiSelect {
        color: var(--text-color, #eff1f3) !important;
    }
    
    p {
        color: var(--text-secondary-color, #d1d5db);
        line-height: 1.6;
    }

    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        color: var(--text-color, #eff1f3);
        margin-bottom: 2rem;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        letter-spacing: -0.02em;
    }
    
    .sub-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: var(--text-color, #eff1f3);
        border-bottom: 2px solid var(--primary-color, #ffa500);
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        letter-spacing: -0.01em;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-color, #eff1f3);
        font-weight: 600;
    }
    
    strong, b {
        color: var(--text-color, #eff1f3);
        font-weight: 600;
    }

    a {
        color: var(--primary-color, #ffa500);
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: var(--primary-hover-color, #ffc107);
        text-decoration: underline;
    }

    code {
        background: rgba(255, 165, 0, 0.15);
        color: var(--primary-color, #ffa500);
        padding: 0.2rem 0.4rem;
        border-radius: 4px;
        font-family: 'Courier New', monospace;
    }

    /* --- CUSTOM BOXES & CARDS WITH FALLBACKS --- */
    .info-box, .success-box, .warning-box {
        color: var(--text-color, #eff1f3);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid var(--primary-color, #ffa500);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        background-color: var(--surface-color, #282828);
    }
    
    .info-box h3, .success-box h3, .warning-box h3 {
        color: var(--text-color, #eff1f3);
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: none;
    }
    
    .info-box p, .info-box ul, .info-box ol,
    .success-box ul, .success-box ol,
    .warning-box ol {
        color: var(--text-secondary-color, #d1d5db);
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }

    blockquote {
        background: var(--surface-color, #282828);
        border-left: 4px solid var(--primary-color, #ffa500);
        padding: 1rem;
        border-radius: 8px;
        color: var(--text-secondary-color, #d1d5db);
    }

    /* --- WIDGETS WITH ENHANCED DEPLOYMENT COMPATIBILITY --- */
    .stButton > button {
        background: var(--primary-color, #ffa500);
        color: var(--bg-color, #1a1a1a);
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
        background: var(--primary-hover-color, #ffc107);
    }

    .stSelectbox > div > div, .stMultiSelect > div > div {
        background: var(--surface-color, #282828);
        border-radius: 8px;
        border: 1px solid var(--border-color, #3d3d3d);
        color: var(--text-color, #eff1f3);
    }
    
    .stCheckbox > div > div { 
        color: var(--text-color, #eff1f3); 
    }
    
    .stProgress > div > div > div {
        background: var(--primary-color, #ffa500);
    }
    
    .streamlit-expanderHeader {
        background: var(--surface-color, #282828);
        color: var(--text-color, #eff1f3);
        border-radius: 8px;
        font-weight: 500;
        border: 1px solid var(--border-color, #3d3d3d);
    }

    .stAlert {
        border-radius: 8px;
        background-color: var(--surface-color, #282828);
    }
    
    /* Chart container styling with fallbacks */
    .js-plotly-plot {
        background: var(--surface-color, #282828) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        box-sizing: border-box !important;
        max-width: 100% !important;
        overflow-x: auto !important;
    }

    /* --- CHAT INTERFACE STYLING WITH FALLBACKS --- */
    .stChatMessage {
        background-color: var(--surface-color, #282828) !important;
        border: 1px solid var(--border-color, #3d3d3d) !important;
        border-radius: 12px !important;
        margin-bottom: 1rem !important;
        padding: 1rem !important;
    }

    .stChatMessage[data-testid="chatMessage"] {
        background-color: rgba(255, 165, 0, 0.1) !important;
        border-left: 4px solid var(--primary-color, #ffa500) !important;
    }

    .stChatMessage[data-testid="chatMessage"] .stChatMessageContent {
        color: var(--text-color, #eff1f3) !important;
    }

    .stTextArea textarea {
        background-color: var(--surface-color, #282828) !important;
        color: var(--text-color, #eff1f3) !important;
        border: 1px solid var(--border-color, #3d3d3d) !important;
        border-radius: 8px !important;
    }

    /* Enhanced form styling */
    .stForm {
        background: var(--surface-color, #282828) !important;
        border: 1px solid var(--border-color, #3d3d3d) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
    }

    /* --- ENHANCED CHAT BUTTON STYLING --- */
    
    /* Primary chat buttons (Send Question) - Vibrant Green */
    .stForm .stButton > button[data-testid="baseButton-primary"] {
        background: linear-gradient(135deg, #00d084, #00b574) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(0, 208, 132, 0.3) !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
    }

    .stForm .stButton > button[data-testid="baseButton-primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(0, 208, 132, 0.4) !important;
        background: linear-gradient(135deg, #00b574, #009963) !important;
    }

    /* Secondary chat buttons (Clear) - Elegant Purple */
    .stForm .stButton > button[data-testid="baseButton-secondary"] {
        background: linear-gradient(135deg, #8b5cf6, #7c3aed) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        box-shadow: 0 2px 10px rgba(139, 92, 246, 0.2) !important;
    }

    .stForm .stButton > button[data-testid="baseButton-secondary"]:hover {
        background: linear-gradient(135deg, #7c3aed, #6d28d9) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3) !important;
    }

    /* Suggested question buttons - Clean transparent style with border on hover */
    .stButton > button:not([data-testid="baseButton-primary"]):not([data-testid="baseButton-secondary"]),
    div[data-testid="column"] .stButton > button,
    .stButton button {
        background: transparent !important;
        background-color: transparent !important;
        background-image: none !important;
        color: var(--text-color, #eff1f3) !important;
        border: 1px solid var(--border-color, #3d3d3d) !important;
        border-radius: 8px !important;
        padding: 0.75rem 1rem !important;
        font-weight: 400 !important;
        transition: all 0.3s ease !important;
        text-align: left !important;
        white-space: normal !important;
        height: auto !important;
        min-height: 3rem !important;
        box-shadow: none !important;
    }

    .stButton > button:not([data-testid="baseButton-primary"]):not([data-testid="baseButton-secondary"]):hover,
    div[data-testid="column"] .stButton > button:hover,
    .stButton button:hover {
        background: rgba(59, 130, 246, 0.1) !important;
        background-color: rgba(59, 130, 246, 0.1) !important;
        background-image: none !important;
        color: #3b82f6 !important;
        border: 1px solid #3b82f6 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 2px 10px rgba(59, 130, 246, 0.15) !important;
    }

    /* Override any Streamlit default button styling specifically for suggested questions */
    .stButton > button[kind="secondary"] {
        background: transparent !important;
        background-color: transparent !important;
        background-image: none !important;
        border: 1px solid var(--border-color, #3d3d3d) !important;
    }

    /* Force override any orange/amber backgrounds */
    .stButton > button:not([type="submit"]):not([data-testid="baseButton-primary"]) {
        background: transparent !important;
        background-color: transparent !important;
        background-image: none !important;
    }

    /* Chat management buttons (Clear History, Export) - Sophisticated styling */
    .stButton > button:contains("Clear Chat History") {
        background: linear-gradient(135deg, #ef4444, #dc2626) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        box-shadow: 0 2px 10px rgba(239, 68, 68, 0.2) !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:contains("Clear Chat History"):hover {
        background: linear-gradient(135deg, #dc2626, #b91c1c) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3) !important;
    }

    .stButton > button:contains("Export Chat") {
        background: linear-gradient(135deg, #f59e0b, #d97706) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        box-shadow: 0 2px 10px rgba(245, 158, 11, 0.2) !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:contains("Export Chat"):hover {
        background: linear-gradient(135deg, #d97706, #b45309) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3) !important;
    }

    /* Download button styling - Teal theme */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #14b8a6, #0d9488) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        box-shadow: 0 2px 10px rgba(20, 184, 166, 0.2) !important;
        transition: all 0.3s ease !important;
    }

    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #0d9488, #0f766e) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 15px rgba(20, 184, 166, 0.3) !important;
    }

    /* Chat message text styling */
    .stChatMessage p, .stChatMessage div {
        color: var(--text-color, #eff1f3) !important;
    }

    /* Chat message code blocks */
    .stChatMessage pre {
        background: rgba(59, 130, 246, 0.15) !important;
        color: #3b82f6 !important;
        border: 1px solid var(--border-color, #3d3d3d) !important;
        border-radius: 4px !important;
        padding: 0.5rem !important;
    }

    /* Chat message lists */
    .stChatMessage ul, .stChatMessage ol {
        color: var(--text-secondary-color, #d1d5db) !important;
    }

    /* Chat message links */
    .stChatMessage a {
        color: #3b82f6 !important;
    }

    .stChatMessage a:hover {
        color: #2563eb !important;
    }

    /* --- ANIMATIONS --- */
    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.02); }
        100% { opacity: 1; transform: scale(1); }
    }

    .pulse { animation: pulse 2s infinite; }

    /* Error and warning message styling */
    .stError, .stWarning, .stInfo, .stSuccess {
        border-radius: 8px !important;
        border: none !important;
    }
    
    /* Ensure visibility of all text elements */
    * {
        box-sizing: border-box;
    }
    
    /* Force visibility for critical elements */
    .stSelectbox label, .stMultiSelect label, .stTextArea label {
        color: var(--text-color, #eff1f3) !important;
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Header
    st.markdown('<h1 class="main-header">📚 DSA Learning Assistant</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🎯 Navigation")
        page = st.selectbox(
            "Choose a page",
            ["🏠 Home", "📚 Study Plan", "🧩 Problem Suggestions", "💬 Chat", "ℹ️ About"]
        )
        
        st.markdown("---")
        st.markdown("### 💡 How it works")
        st.info("**Smart Learning Paths**\n\n"
                "• Select your target topic\n"
                "• Mark topics you already know\n"
                "• Get personalized study path\n"
                "• Practice with curated problems\n"
                "• Track your progress")
    
    # Initialize graph with error handling for deployment
    try:
        if 'topic_graph' not in st.session_state:
            st.session_state.topic_graph = TopicGraph(TOPIC_DEPENDENCIES)
        if 'topological_sort' not in st.session_state:
            st.session_state.topological_sort = TopologicalSort(TOPIC_DEPENDENCIES)
    except Exception as e:
        st.error(f"Error initializing graph system: {str(e)}")
        st.info("Please refresh the page to retry initialization.")
        return
    
    # Page routing with error handling
    try:
        if page == "🏠 Home":
            show_home_page()
        elif page == "📚 Study Plan":
            show_study_plan()
        elif page == "🧩 Problem Suggestions":
            show_problem_suggestions()
        elif page == "💬 Chat":
            show_chat_interface()
        elif page == "ℹ️ About":
            show_about_page()
    except Exception as e:
        st.error(f"Error loading page: {str(e)}")
        st.info("Please try refreshing the page or selecting a different option.")

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
        <li><strong>AI Chat Assistant:</strong> Ask questions and get instant help with DSA concepts</li>
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
        <li>Ask questions in the <strong>AI Chat</strong> section</li>
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
    
    # Use responsive columns with better mobile handling
    try:
        col1, col2 = st.columns([1, 1])
    except:
        # Fallback to single column layout if columns fail
        col1 = st.container()
        col2 = st.container()
    
    with col1:
        # Target topic selection
        try:
            all_topics = get_all_topics()
            target_topic = create_topic_selector(all_topics, "target_topic", "Select topic you want to learn")
        except Exception as e:
            st.error(f"Error loading topics: {str(e)}")
            return
    
    with col2:
        # Known topics selection
        try:
            known_topics = create_multi_topic_selector(all_topics, "known_topics", "Select topics you already know")
        except Exception as e:
            st.error(f"Error loading topic selector: {str(e)}")
            known_topics = []
    
    # Generate learning path
    if target_topic and validate_topic_selection(target_topic, all_topics):
        st.markdown("---")
        
        try:
            # Get learning path
            learning_path = st.session_state.topic_graph.get_learning_path(target_topic, known_topics)
            
            # Display results
            st.subheader("📚 Your Personalized Learning Path")
            st.markdown(format_learning_path(learning_path))
            
            # Learning path visualization with fallback
            if learning_path:
                try:
                    fig = create_learning_path_chart(learning_path)
                    if fig:
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        # Fallback: Simple text-based visualization
                        st.info("📊 Chart visualization unavailable. Here's your learning path:")
                        for i, topic in enumerate(learning_path, 1):
                            st.write(f"**Step {i}:** {topic}")
                except Exception as e:
                    st.warning(f"Visualization error: {str(e)}. Showing simplified view.")
                    # Simple fallback visualization
                    st.info("📊 Learning Path Steps:")
                    for i, topic in enumerate(learning_path, 1):
                        st.write(f"**{i}.** {topic}")
            
        except Exception as e:
            st.error(f"Error generating learning path: {str(e)}")
            return
        
        # Topic information section
        st.markdown("---")
        st.subheader(f"ℹ️ About {target_topic}")
        
        try:
            # Get topic details
            description = get_topic_description(target_topic)
            dependencies = st.session_state.topic_graph.get_prerequisites(target_topic)
            dependents = st.session_state.topic_graph.get_dependent_topics(target_topic)
            
            # Use responsive layout with fallback
            try:
                col1, col2 = st.columns([1, 1])
            except:
                col1 = st.container()
                col2 = st.container()
            
            with col1:
                display_topic_info(target_topic, description, dependencies)
            
            with col2:
                st.subheader(f"📤 Topics that depend on {target_topic}")
                if dependents:
                    for dep in dependents:
                        st.write(f"• {dep}")
                else:
                    st.write("No topics depend on this one (it's a leaf node)")
        
        except Exception as e:
            st.warning(f"Error loading topic information: {str(e)}")
        
        # Category information
        try:
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
        except Exception as e:
            st.warning(f"Error loading category information: {str(e)}")

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

def show_chat_interface():
    """Display the chat interface"""
    
    st.markdown('<h2 class="sub-header">💬 AI Chat Assistant</h2>', unsafe_allow_html=True)
    
    # Create chat interface
    chat = create_gemini_chat_interface()
    
    if chat:
        display_chat_interface(chat)
    else:
        st.info("Please add your Gemini API key to use the chat feature.")

if __name__ == "__main__":
    main() 