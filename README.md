# Sudoku Solver with Graph Coloring and Backtracking

This repository contains a Python-based Sudoku solver that leverages **graph theory**, **graph coloring**, and **backtracking** techniques to efficiently solve Sudoku puzzles. The project is designed with modular, object-oriented principles to ensure clarity and extensibility.

## Features

- **Graph Representation**: 
  - The Sudoku grid is represented as a graph where each cell is a node, and constraints are modeled as edges.
- **Graph Coloring**:
  - Each number (1–9) represents a color, and the problem is solved by assigning colors to nodes such that no two connected nodes share the same color.
- **Backtracking**:
  - Ensures all constraints are met while recursively finding the solution.
- **Customizable**:
  - Easily input Sudoku puzzles as a 9x9 grid or array.

---

## Getting Started

### Prerequisites

- **Python 3.8+** is required.
- Install additional dependencies if necessary:
  ```
  pip install -r requirements.txt
  ```
- Clone repository
  ```
  git clone https://github.com/Yazzine02/Sudoku-color-graph-resolution.git
  ```
- Run solver
  ```
  python main.py
  ```
