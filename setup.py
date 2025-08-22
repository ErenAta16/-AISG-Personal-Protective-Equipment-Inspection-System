#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AISG KKD Denetim Sistemi
AI-powered safety monitoring system for personal protective equipment detection
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Get version from __init__.py
def get_version():
    version_file = os.path.join("aisg", "__init__.py")
    if os.path.exists(version_file):
        with open(version_file, "r", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("__version__"):
                    return line.split("=")[1].strip().strip('"\'')
    return "1.0.0"

setup(
    name="aisg-kkd-denetim",
    version=get_version(),
    author="MCBU XRLab Team",
    author_email="xrlab@mcbu.edu.tr",
    description="AI-powered safety monitoring system for personal protective equipment detection",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/aisg-kkd-denetim-sistemi",
    project_urls={
        "Bug Reports": "https://github.com/username/aisg-kkd-denetim-sistemi/issues",
        "Source": "https://github.com/username/aisg-kkd-denetim-sistemi",
        "Documentation": "https://github.com/username/aisg-kkd-denetim-sistemi#readme",
        "Funding": "https://github.com/sponsors/username",
    },
    packages=find_packages(include=["aisg", "aisg.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Manufacturing",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Computer Vision",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Safety",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "pytest-mock>=3.0",
            "flake8>=3.8",
            "black>=21.0",
            "isort>=5.0",
            "mypy>=0.800",
            "bandit>=1.6",
            "safety>=1.10",
            "pre-commit>=2.15",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.15",
            "sphinx-autodoc-typehints>=1.12",
        ],
        "deploy": [
            "gunicorn>=20.0",
            "supervisor>=4.0",
            "nginx>=1.18",
        ],
    },
    entry_points={
        "console_scripts": [
            "aisg=aisg.cli:main",
            "aisg-server=aisg.server:main",
            "aisg-train=aisg.training:main",
        ],
    },
    include_package_data=True,
    package_data={
        "aisg": [
            "models/*.pt",
            "config/*.yaml",
            "config/*.json",
            "templates/*.html",
            "static/*",
        ],
    },
    zip_safe=False,
    keywords=[
        "computer vision",
        "object detection",
        "safety monitoring",
        "PPE detection",
        "industrial safety",
        "YOLOv8",
        "Flask",
        "OpenCV",
        "AI",
        "machine learning",
        "deep learning",
        "computer vision",
        "safety",
        "monitoring",
        "detection",
    ],
    platforms=["any"],
    license="MIT",
    maintainer="MCBU XRLab Team",
    maintainer_email="xrlab@mcbu.edu.tr",
    download_url="https://github.com/username/aisg-kkd-denetim-sistemi/archive/v1.0.0.tar.gz",
    provides=["aisg"],
    requires_python=">=3.8",
    setup_requires=[
        "setuptools>=45",
        "wheel",
        "setuptools_scm[toml]>=6.2",
    ],
    use_scm_version=True,
    setup_cfg=True,
)
