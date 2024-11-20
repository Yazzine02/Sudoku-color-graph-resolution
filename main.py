from models.Graph import Graph

def main():
    # 0 represents empty cells
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    graph = Graph()

    # Populate the graph
    for row in range(9):
        for col in range(9):
            node_id = board[row][col]
            graph.add_node(row, col, node_id)
    # Solve Sudoku
    if graph.solve_sudoku():
        print("Sudoku solved successfully")
    else:
        print("No solution exists for the given Sudoku.")
    graph.display_graph()


if __name__ == "__main__":
    main()
