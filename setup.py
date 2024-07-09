rom setuptools import setup, find_packages

setup(
    name='wrappers',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'dependency1',
        'dependency2',
        'numpy',                    # Fundamental package for scientific computing with Python
        'pandas',                   # Data manipulation and analysis
        'requests',                 # HTTP library for making requests to external resources
        'matplotlib',               # Plotting library for creating visualizations
        'scipy',                    # Scientific library for mathematics, science, and engineering
        'scikit-learn',             # Machine learning library for classical ML algorithms
        'tensorflow',               # Deep learning library for neural networks
        'torch',                    # PyTorch deep learning framework
        'flask',                    # Lightweight web framework for creating APIs or web applications
        'django',                   # High-level Python web framework for rapid development
        'sqlalchemy',               # SQL toolkit and Object-Relational Mapping (ORM) library
        'beautifulsoup4',           # Library for parsing HTML and XML documents
        'pyyaml',                   # YAML parser and emitter
        'pytest',                   # Testing framework
        'coverage',                 # Code coverage measurement
        'pytest-cov',               # Plugin for pytest to generate coverage reports
        'tox',                      # Virtual environment management and testing tool
        'sphinx',                   # Documentation generator
        'sphinx-rtd-theme',         # Read-the-docs theme for Sphinx
        'wheel',                    # Built-package format for Python
        'setuptools',               # Library to facilitate packaging Python projects
        'twine',                    # Utility for interacting with PyPI
    ],
    author='Nadhiya D',
    author_email='nadhiyad.05@gmail.com',
    description='Installation setup for wrappers project',
    url='https://github.com/nadhiyad/Amazon_review',
    license='MIT',
)