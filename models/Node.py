class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.connectedTo = {} # set of neighbor_id : position

    def add_neighbor(self, neighbor_id, neighbor_position):
        if neighbor_id not in self.connectedTo.keys():
            self.connectedTo[neighbor_id] =  neighbor_position

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def __str__(self):
        connections = ', '.join(f"{neighbor_id} at {pos}" for neighbor_id, pos in self.connectedTo.items())
        return f"Node {self.id} Connected to: [{connections}]"