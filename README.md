# DSA Topic Recommendation System

A web application that helps users identify the optimal learning path for DSA topics using graph algorithms.

## Features

- **Topic Dependency Analysis**: Uses topological sorting to determine prerequisite topics
- **Learning Path Generation**: Suggests the best order to study topics
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
│   │   └── topic_data.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── app/
│   ├── __init__.py
│   └── main.py
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
3. Run the application:
   ```bash
   streamlit run app/main.py
   ```

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. **Push your code to GitHub**
2. **Visit [share.streamlit.io](https://share.streamlit.io)**
3. **Connect your GitHub repository**
4. **Set main file path to: `app/main.py`**
5. **Deploy!**

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

## Usage

1. Select the topic you want to study
2. The system will analyze dependencies and suggest prerequisite topics
3. Get a recommended learning path

## Future Enhancements

- User knowledge assessment
- Personalized learning paths
- AI-powered question recommendations
- LeetCode integration 