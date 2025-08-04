# Dependency-Graph-Viewer
A Python tool that reads a list of package dependencies (and sub-dependencies) from a text file and generates a colorful dependency graph using NetworkX and Matplotlib.

## Features
- Parses ```dependencies.txt``` and visualizes packages and their sub-dependencies
- Highlights main dependencies with bold colors and sub-dependencies with matching lighter colors
- Automatically sizes nodes based on the number of sub-dependencies
- Supports light and dark themes
- Shared sub-dependencies are highlighted in pink

## File Format
The tool expects a dependencies.txt file structured like:
```
matplotlib==3.10.5
  - contourpy [required: >=1.0.1, installed: 1.3.3]
    - numpy [required: >=1.25, installed: 2.3.2]
  - cycler [required: >=0.10, installed: 0.12.1]
  - fonttools [required: >=4.22.0, installed: 4.59.0]
  - kiwisolver [required: >=1.3.1, installed: 1.4.8]
  - numpy [required: >=1.23, installed: 2.3.2]
  - packaging [required: >=20.0, installed: 25.0]
  - pillow [required: >=8, installed: 11.3.0]
  - pyparsing [required: >=2.3.1, installed: 3.2.3]
  - python-dateutil [required: >=2.7, installed: 2.9.0.post0]
    - six [required: >=1.5, installed: 1.17.0]
networkx==3.5
pandas==2.3.1
  - numpy [required: >=1.26.0, installed: 2.3.2]
  - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
    - six [required: >=1.5, installed: 1.17.0]
  - pytz [required: >=2020.1, installed: 2025.2]
  - tzdata [required: >=2022.7, installed: 2025.2]
pipdeptree==2.28.0
  - packaging [required: >=24.1, installed: 25.0]
  - pip [required: >=24.2, installed: 25.1.1]
scikit-learn==1.7.1
  - numpy [required: >=1.22.0, installed: 2.3.2]
  - scipy [required: >=1.8.0, installed: 1.16.1]
    - numpy [required: >=1.25.2,<2.6, installed: 2.3.2]
  - joblib [required: >=1.2.0, installed: 1.5.1]
  - threadpoolctl [required: >=3.1.0, installed: 3.6.0]
```
To generate this file, I used ```pipdeptree > dependencies.txt```

## Requirements
- Python 3.8+
- Matplotlib
- NetworkX
- Pipdeptree

```pip install networkx matplotlib pipdeptree```

You may also install any other packages you would like to test it

## Examples
![Light Theme Dependency Tree](https://github.com/ethanposey/Dependency-Graph-Viewer/blob/main/light_dep_tree.png)
![Dark Theme Dependency Tree](https://github.com/ethanposey/Dependency-Graph-Viewer/blob/main/dark_dep_tree.png)
