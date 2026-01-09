"""
Setup script for Axiom CLI tool
"""
from setuptools import setup, find_packages

setup(
    name="axiom-cli",
    version="0.1.0",
    description="AI-Powered Repository Analysis and Deployment Advisor",
    author="Mangesh",
    author_email="mangeshbhalerao523@gmail.com",
    url="https://github.com/MangeshBhalerao/Axiom",
    packages=find_packages(),
    py_modules=['analyze', 'recognize', 'signature', 'orchestrator', 'cli'],
    entry_points={
        'console_scripts': [
            'axiom=cli:main',
        ],
    },
    install_requires=[
        # Add dependencies here as you add them
        # 'requests',
        # 'click',
        # 'rich',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires='>=3.8',
)
