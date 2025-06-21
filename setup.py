from setuptools import setup, find_packages

setup(
    name="dsa-helper",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0,<2.0.0",
        "networkx>=3.0,<4.0",
        "pandas>=2.0.0,<3.0.0",
        "matplotlib>=3.7.0,<4.0.0",
        "plotly>=5.15.0,<6.0.0",
    ],
    python_requires=">=3.8",
) 