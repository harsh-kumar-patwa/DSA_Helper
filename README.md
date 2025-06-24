# DSA Learning Assistant

A comprehensive web application that helps users identify the optimal learning path for DSA topics using graph algorithms and provides AI-powered chat assistance for DSA questions.

## Deployed Link : https://harshkumarpatwa-dsa.streamlit.app/

## Demo Video : https://www.loom.com/share/482c038bd14a4d81a9c5663cb6aa4380?sid=f301e52f-0405-4921-8047-7f60e77f4812

## Features

- **Topic Dependency Analysis**: Uses topological sorting to determine prerequisite topics
- **Learning Path Generation**: Suggests the best order to study topics
- **AI Chat Assistant**: Ask questions and get instant help with DSA concepts using Gemini AI
- **Problem Suggestions**: Curated practice problems by difficulty level
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Graph-based Backend**: Python implementation using graph algorithms

## Project Structure

```
DSA_1_project/
├── src/
│   ├── __init__.py
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── topic_graph.py
│   │   └── topological_sort.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── topic_data.py
│   │   └── problem_data.py
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       └── gemini_chat.py
├── app/
│   ├── __init__.py
│   └── main.py
├── .streamlit/
│   └── secrets.toml
├── requirements.txt
├── README.md
└── .gitignore
```

## Algorithm Used

**Topological Sorting**: This algorithm is used to find the optimal learning order of topics by:
1. Creating a directed acyclic graph (DAG) where nodes represent topics
2. Edges represent dependencies (prerequisites)
3. Topological sort provides the order in which topics should be studied

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Gemini API key (for chat feature):
   - Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Add it to `.streamlit/secrets.toml`:
     ```toml
     GEMINI_API_KEY = "your_api_key_here"
     ```
4. Run the application:
   ```bash
   streamlit run app/main.py
   ```

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. **Push your code to GitHub**
2. **Visit [share.streamlit.io](https://share.streamlit.io)**
3. **Connect your GitHub repository**
4. **Set main file path to: `app/main.py`**
5. **Add your Gemini API key in the Streamlit Cloud secrets**
6. **Deploy!**

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

## Usage

1. **Study Plan**: Select the topic you want to study and get personalized learning paths
2. **Problem Suggestions**: Practice with curated problems by difficulty level
3. **AI Chat**: Ask questions about DSA concepts and get instant AI-powered help
4. **Progress Tracking**: Monitor your learning progress

## AI Chat Feature

The AI Chat Assistant uses Google's Gemini AI to provide:
- **Concept Explanations**: Clear, step-by-step explanations of DSA concepts
- **Code Examples**: Practical code examples in Python, Java, or C++
- **Complexity Analysis**: Time and space complexity explanations
- **Practice Problems**: Suggested exercises and problems
- **Learning Guidance**: Personalized advice for your DSA journey

### Setting up the Chat Feature

1. Get a free Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add the API key to your Streamlit secrets:
   - Local development: Add to `.streamlit/secrets.toml`
   - Streamlit Cloud: Add in the app's secrets management
3. Restart the application

## Future Enhancements

- User knowledge assessment
- Personalized learning paths based on performance
- Integration with more coding platforms
- Advanced progress analytics
- Mobile application
- Community discussion forums 
