"""
Setup configuration for CoEvolution Toolkit
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="coevolution-toolkit",
    version="1.0.0",
    author="CoEvolution Framework Contributors",
    author_email="coevolution@example.com",  # Update with actual email
    description="Python toolkit for analyzing visible-dark matter coevolution in galaxies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/coevolution-toolkit",  # Update with actual URL
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/coevolution-toolkit/issues",
        "Documentation": "https://github.com/yourusername/coevolution-toolkit/blob/main/README.md",
        "Source Code": "https://github.com/yourusername/coevolution-toolkit",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
            "sphinx>=5.0",
            "sphinx-rtd-theme>=1.0",
        ],
        "notebooks": [
            "jupyter>=1.0",
            "notebook>=6.0",
            "ipywidgets>=8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "coevolution-demo=coevolution_toolkit.examples:run_demo",
        ],
    },
    include_package_data=True,
    package_data={
        "coevolution_toolkit": ["data/*.txt", "examples/*.py"],
    },
    keywords="cosmology dark-matter galaxies astrophysics coevolution feedback",
    zip_safe=False,
)
