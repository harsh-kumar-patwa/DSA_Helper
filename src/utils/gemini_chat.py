"""
Gemini Chat Integration for DSA Questions
Provides AI-powered chat functionality for DSA learning assistance
"""

import google.generativeai as genai
import streamlit as st
from typing import List, Dict, Optional
import os
import random
import time

class GeminiChat:
    def __init__(self, api_key: str):
        """
        Initialize Gemini chat with API key
        
        Args:
            api_key: Google Gemini API key
        """
        self.api_key = api_key
        genai.configure(api_key=api_key)
        
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # System prompt for DSA context
        self.system_prompt = """
        You are an expert Data Structures and Algorithms (DSA) tutor and mentor. 
        Your role is to help students understand DSA concepts, solve problems, and 
        provide guidance on their learning journey.
        
        Key guidelines:
        1. Provide clear, step-by-step explanations
        2. Use code examples when relevant (preferably in Python, Java, or C++)
        3. Explain time and space complexity when discussing algorithms
        4. Suggest related topics or concepts for further learning
        5. Be encouraging and supportive
        6. If a question is not DSA-related, politely redirect to DSA topics
        7. Use analogies and real-world examples when helpful
        8. Provide practice problems or exercises when appropriate
        
        Always maintain a helpful, educational tone and focus on DSA learning.
        """
        
        # Initialize chat history
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
    
    def get_response(self, user_message: str) -> str:
        """
        Get response from Gemini for user message
        
        Args:
            user_message: User's question or message
            
        Returns:
            AI response as string
        """
        try:
            # Create chat session
            chat = self.model.start_chat(history=[])
            
            # Prepare the full prompt
            full_prompt = f"{self.system_prompt}\n\nUser Question: {user_message}"
            
            # Get response
            response = chat.send_message(full_prompt)
            
            # Add to chat history
            st.session_state.chat_history.append({
                'user': user_message,
                'assistant': response.text
            })
            
            return response.text
            
        except Exception as e:
            error_msg = f"Sorry, I encountered an error: {str(e)}"
            st.error(error_msg)
            return error_msg
    
    def get_chat_history(self) -> List[Dict[str, str]]:
        """
        Get chat history
        
        Returns:
            List of chat messages
        """
        return st.session_state.chat_history
    
    def clear_history(self):
        """Clear chat history"""
        st.session_state.chat_history = []
        if 'user_input' in st.session_state:
            st.session_state.user_input = ""
    
    def get_suggested_questions(self) -> List[str]:
        """
        Get suggested DSA questions for users
        
        Returns:
            List of suggested questions
        """
        return [
            "What is the difference between arrays and linked lists?",
            "How does quicksort work and what's its time complexity?",
            "Can you explain dynamic programming with an example?",
            "What are the advantages of using a hash table?",
            "How do I implement a binary search tree?",
            "What's the difference between BFS and DFS?",
            "Can you help me understand time complexity analysis?",
            "What are some common graph algorithms?",
            "How do I approach solving algorithm problems?",
            "What's the best way to learn data structures?"
        ]

def get_motivational_quotes():
    """
    Get random motivational DSA quotes
    
    Returns:
        List of motivational quotes about DSA learning
    """
    quotes = [
        "💪 **\"The best time to plant a tree was 20 years ago. The second best time is now.\"** - Start your DSA journey today!",
        "🧠 **\"Data structures are not just about organizing data, they're about organizing thoughts.\"** - Think systematically!",
        "🚀 **\"Every expert was once a beginner. Every pro was once an amateur.\"** - Keep practicing algorithms!",
        "⚡ **\"The only way to learn a new programming language is by writing programs in it.\"** - Code your way to mastery!",
        "🎯 **\"First, solve the problem. Then, write the code.\"** - Algorithm thinking comes first!",
        "🔥 **\"The most important property of a program is whether it accomplishes the intention of its user.\"** - Focus on correctness!",
        "💡 **\"Good code is its own best documentation.\"** - Write clean, understandable algorithms!",
        "🌟 **\"Practice doesn't make perfect. Perfect practice makes perfect.\"** - Quality over quantity in DSA!",
        "🎪 **\"The best programs are written so that computing machines can perform them quickly.\"** - Optimize like a pro!",
        "🚪 **\"Every algorithm has a story to tell.\"** - Understand the 'why' behind each solution!",
        "🎨 **\"Programming is an art, and algorithms are the brushstrokes.\"** - Create beautiful solutions!",
        "⏰ **\"Time complexity matters, but understanding matters more.\"** - Master the concepts first!",
        "🎲 **\"In DSA, every problem is a puzzle waiting to be solved.\"** - Embrace the challenge!",
        "🌈 **\"Recursion is not just a technique, it's a way of thinking.\"** - Think in patterns!",
        "🎯 **\"A good algorithm is like a sharp knife - it cuts through complexity.\"** - Keep your solutions clean!"
    ]
    return quotes

def create_gemini_chat_interface():
    """
    Create Streamlit interface for Gemini chat
    
    Returns:
        GeminiChat instance if API key is available
    """
    st.markdown("### 🤖 DSA AI Assistant")
    st.markdown("Ask me anything about Data Structures and Algorithms!")
    
    # Check for API key
    api_key = st.secrets.get("GEMINI_API_KEY", None)
    
    if not api_key:
        st.warning("⚠️ Gemini API key not found. Please add your API key to continue.")
        st.info("To use the AI chat feature, you need to:")
        st.markdown("""
        1. Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
        2. Add it to your Streamlit secrets or environment variables
        3. Restart the application
        """)
        
        # Allow manual input for testing
        with st.expander("🔑 Enter API Key for Testing"):
            api_key = st.text_input("Enter your Gemini API key:", type="password", key="manual_api_key")
        
        if not api_key:
            return None
    
    # Initialize chat
    if 'gemini_chat' not in st.session_state:
        st.session_state.gemini_chat = GeminiChat(api_key)
    
    return st.session_state.gemini_chat

def display_motivational_thinking():
    """Display motivational content while AI is thinking"""
    quotes = get_motivational_quotes()
    selected_quote = random.choice(quotes)
    
    # Create a placeholder for dynamic content
    thinking_placeholder = st.empty()
    
    with thinking_placeholder.container():
        st.markdown("""
        <div class="info-box" style="text-align: center; animation: pulse 2s infinite;">
        <h3>🤔 AI is thinking...</h3>
        """ + selected_quote + """
        </div>
        """, unsafe_allow_html=True)
    
    return thinking_placeholder

def display_chat_interface(chat: GeminiChat):
    """
    Display the chat interface
    
    Args:
        chat: GeminiChat instance
    """
    # Initialize session state for input
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    
    # Suggested questions
    st.markdown("#### 💡 Suggested Questions")
    st.markdown("*Click on any question below to ask it directly:*")
    
    suggested_questions = chat.get_suggested_questions()
    
    # Create columns for suggested questions (responsive layout)
    cols = st.columns(2)
    for i, question in enumerate(suggested_questions):
        col_idx = i % 2
        with cols[col_idx]:
            if st.button(f"💭 {question}", key=f"suggest_{i}", use_container_width=True):
                st.session_state.user_input = question
                st.rerun()
    
    st.markdown("---")
    
    # User input section (moved up for better UX)
    st.markdown("#### 📝 Ask a Question")
    
    # Create input form
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_area(
            "Type your DSA question here:",
            value=st.session_state.user_input,
            height=100,
            placeholder="e.g., How does quicksort work? What's the difference between arrays and linked lists?",
            key="question_input"
        )
        
        col1, col2 = st.columns([3, 1])
        with col1:
            submit_button = st.form_submit_button("🚀 Send Question", type="primary", use_container_width=True)
        with col2:
            clear_input_button = st.form_submit_button("🗑️ Clear", use_container_width=True)
    
    # Handle form submission
    if submit_button and user_input.strip():
        # Clear the session state input
        st.session_state.user_input = ""
        
        # Show motivational content while thinking
        thinking_placeholder = display_motivational_thinking()
        
        try:
            # Get AI response
            response = chat.get_response(user_input.strip())
            
            # Clear the thinking message
            thinking_placeholder.empty()
            
            # Show success message briefly
            success_placeholder = st.empty()
            success_placeholder.success("✅ Got your answer! Check the chat history below.")
            time.sleep(2)
            success_placeholder.empty()
            
            # Rerun to show updated chat
            st.rerun()
            
        except Exception as e:
            thinking_placeholder.empty()
            st.error(f"❌ Sorry, something went wrong: {str(e)}")
    
    elif submit_button and not user_input.strip():
        st.warning("⚠️ Please enter a question before sending!")
    
    elif clear_input_button:
        st.session_state.user_input = ""
        st.rerun()
    
    st.markdown("---")
    
    # Chat history
    st.markdown("#### 💬 Chat History")
    
    chat_history = chat.get_chat_history()
    
    if not chat_history:
        st.info("👋 No messages yet! Start by asking a question above or clicking on a suggested question.")
    else:
        # Display chat history in reverse order (newest first)
        for i, message in enumerate(reversed(chat_history)):
            with st.container():
                # User message
                with st.chat_message("user", avatar="👤"):
                    st.markdown(f"**You:** {message['user']}")
                
                # Assistant message
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(f"**AI Assistant:** {message['assistant']}")
                
                # Add separator except for last message
                if i < len(chat_history) - 1:
                    st.markdown("---")
    
    # Chat controls
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            chat.clear_history()
            st.success("🧹 Chat history cleared!")
            time.sleep(1)
            st.rerun()
    
    with col2:
        if st.button("📤 Export Chat", use_container_width=True):
            if chat_history:
                # Create export text
                export_text = "# DSA Chat History\n\n"
                for i, message in enumerate(chat_history, 1):
                    export_text += f"## Question {i}\n**You:** {message['user']}\n\n**AI:** {message['assistant']}\n\n---\n\n"
                
                st.download_button(
                    label="💾 Download Chat History",
                    data=export_text,
                    file_name="dsa_chat_history.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            else:
                st.info("No chat history to export!") 