"""
Deployment Compatibility Checker
Helps identify potential issues in deployment environments
"""

import streamlit as st
import sys
import os
import importlib
from typing import Dict, List, Tuple

def check_dependencies() -> Dict[str, bool]:
    """
    Check if all required dependencies are available
    
    Returns:
        Dictionary with dependency status
    """
    dependencies = {
        'streamlit': False,
        'networkx': False,
        'pandas': False,
        'matplotlib': False,
        'plotly': False,
        'google.generativeai': False
    }
    
    for dep in dependencies:
        try:
            importlib.import_module(dep)
            dependencies[dep] = True
        except ImportError:
            dependencies[dep] = False
    
    return dependencies

def check_environment() -> Dict[str, str]:
    """
    Check environment variables and settings
    
    Returns:
        Dictionary with environment information
    """
    env_info = {
        'Python Version': sys.version,
        'Platform': sys.platform,
        'Working Directory': os.getcwd(),
        'STREAMLIT_SERVER_HEADLESS': os.environ.get('STREAMLIT_SERVER_HEADLESS', 'Not Set'),
        'STREAMLIT_BROWSER_GATHER_USAGE_STATS': os.environ.get('STREAMLIT_BROWSER_GATHER_USAGE_STATS', 'Not Set')
    }
    
    return env_info

def check_file_paths() -> Dict[str, bool]:
    """
    Check if all required files exist
    
    Returns:
        Dictionary with file existence status
    """
    required_files = {
        'app/main.py': False,
        'src/data/topic_data.py': False,
        'src/data/problem_data.py': False,
        'src/graph/topic_graph.py': False,
        'src/utils/helpers.py': False,
        'requirements.txt': False,
        '.streamlit/config.toml': False
    }
    
    for file_path in required_files:
        required_files[file_path] = os.path.exists(file_path)
    
    return required_files

def test_chart_creation():
    """
    Test if chart creation works in current environment
    
    Returns:
        Tuple of (success, error_message)
    """
    try:
        import plotly.express as px
        import pandas as pd
        
        # Test basic chart creation
        df = pd.DataFrame({
            'x': [1, 2, 3],
            'y': ['A', 'B', 'C']
        })
        
        fig = px.bar(df, x='x', y='y')
        return (True, "Chart creation successful")
        
    except Exception as e:
        return (False, f"Chart creation failed: {str(e)}")

def test_session_state():
    """
    Test session state functionality
    
    Returns:
        Tuple of (success, error_message)
    """
    try:
        if 'test_key' not in st.session_state:
            st.session_state.test_key = "test_value"
        
        if st.session_state.test_key == "test_value":
            return (True, "Session state working correctly")
        else:
            return (False, "Session state not persisting values")
            
    except Exception as e:
        return (False, f"Session state error: {str(e)}")

def run_deployment_check():
    """
    Run comprehensive deployment compatibility check
    """
    st.subheader("🔍 Deployment Compatibility Check")
    
    # Check dependencies
    st.write("**📦 Dependencies:**")
    deps = check_dependencies()
    for dep, status in deps.items():
        status_icon = "✅" if status else "❌"
        st.write(f"{status_icon} {dep}")
    
    if not all(deps.values()):
        st.error("Some dependencies are missing! Check requirements.txt")
    else:
        st.success("All dependencies are available")
    
    st.markdown("---")
    
    # Check environment
    st.write("**🌍 Environment:**")
    env_info = check_environment()
    for key, value in env_info.items():
        st.write(f"**{key}:** {value}")
    
    st.markdown("---")
    
    # Check file paths
    st.write("**📁 Required Files:**")
    files = check_file_paths()
    for file_path, exists in files.items():
        status_icon = "✅" if exists else "❌"
        st.write(f"{status_icon} {file_path}")
    
    if not all(files.values()):
        st.error("Some required files are missing!")
    else:
        st.success("All required files are present")
    
    st.markdown("---")
    
    # Test chart creation
    st.write("**📊 Chart Creation Test:**")
    chart_success, chart_msg = test_chart_creation()
    if chart_success:
        st.success(chart_msg)
    else:
        st.error(chart_msg)
    
    st.markdown("---")
    
    # Test session state
    st.write("**💾 Session State Test:**")
    session_success, session_msg = test_session_state()
    if session_success:
        st.success(session_msg)
    else:
        st.error(session_msg)
    
    st.markdown("---")
    
    # Overall status
    all_checks = [
        all(deps.values()),
        all(files.values()),
        chart_success,
        session_success
    ]
    
    if all(all_checks):
        st.success("🎉 All compatibility checks passed! Your app should work in deployment.")
    else:
        st.warning("⚠️ Some checks failed. These issues might cause problems in deployment.")
        st.info("Review the failed checks above and fix the issues before deploying.")

if __name__ == "__main__":
    run_deployment_check() 