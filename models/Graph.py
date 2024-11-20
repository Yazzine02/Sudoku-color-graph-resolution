from models.Node import Node


class Graph:
    def __init__(self):
        # dictionary of (row, col) : Node
        self.nodes = {}

    # Helper method to use when adding a node
    def is_valid_position(self, node_row, node_col, node_id):
        # Check row and column validity by fixing row (resp column) and iterating the indexes
        for i in range(9):
            # Check row
            if (node_row, i) in self.nodes and self.nodes[(node_row, i)].get_id() == node_id:
                return False
            # Check column
            if (i, node_col) in self.nodes and self.nodes[(i, node_col)].get_id() == node_id:
                return False
        # Check 3x3 subgrid validity
        # Divise by 3 to get subgrids and multiply by 3 to get the index of beginning of the subgrid in the array
        start_row, start_col = 3*(node_row//3), 3*(node_col//3)
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if (i, j) in self.nodes and self.nodes[(i, j)].get_id() == node_id:
                    return False
        return True

    def add_node(self, node_row, node_column, node_id):
        position = (node_row, node_column)
        # The node needs to not be empty and be valid
        if node_id!=0 and not self.is_valid_position(node_row, node_column, node_id):
            print(f"Node with ID {node_id} at {position} violates constraints.")
            return False
        elif position not in self.nodes:
            self.nodes[position] = Node(node_id)
            return True
        else:
            print(f"Position {position} is already occupied.")
            return False

    def add_edge(self,  position1, position2):
        node1 = self.nodes.get(position1)
        node2 = self.nodes.get(position2)

        if node1 and node2:
            node1.add_neighbor(node2.get_id(), position2)
            node2.add_neighbor(node1.get_id(), position1)

    def find_empty_cell(self):
        # Returns the first empty node found
        for position, node in self.nodes.items():
            if node.get_id() == 0:
                return position
        return None

    def solve_sudoku(self):
        # Find an empty cell
        empty_position = self.find_empty_cell()
        # If no empty cell then the sudoku is filled
        if empty_position is None:
            return True # Solved
        empty_row, empty_col = empty_position
        # We can only fill in with { 1, 2, 3, ..., 9 }
        for num in range(1,10):
            # Check if the empty cell can be filled with a node of number=num
            if self.is_valid_position(empty_row, empty_col, num):
                # No need to instantiate a whole Node
                self.nodes[(empty_row, empty_col)].id= num
                # Solve the rest of the sudoku recursively
                # If recursion true then do it until the end and return true
                if self.solve_sudoku():
                    return True
                else:
                    # Reset
                    self.nodes[(empty_row, empty_col)].id = 0
        return False


    def get_node(self, row, col):
        return self.nodes.get((row, col))

    def display_graph(self):
        for row in range(9):
            row_values = []
            for col in range(9):
                node = self.get_node(row, col)
                row_values.append(node.get_id() if node else 0)
            print(" ".join(map(str, row_values)))