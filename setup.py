from setuptools import setup, find_packages

setup(
    name="nightingale",
    version="0.1.0",
    description="A Python package for prioritizing GitHub issues using the Command pattern",
    author="Kristian Garza",
    author_email="kj.garza@gmail.com",
    url="https://github.com/kjgarza/nightingale",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "nightingale=nightingale.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)