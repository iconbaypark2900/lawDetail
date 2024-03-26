# Defines an EdgeNode class to represent edge nodes in a networked document management system.
class EdgeNode:
    def __init__(self, name):
        self.name = name  # Name of the edge node.
        self.documents = {}  # Dictionary to store documents by their ID.

    # Method to update or add a document in this edge node.
    def update_document(self, doc_id, content):
        self.documents[doc_id] = content  # Update the document content.
        print(f"Document {doc_id} updated at {self.name}")  # Print confirmation message.

# Defines a CentralRepository class for managing the central storage of documents.
class CentralRepository:
    def __init__(self):
        self.documents = {}  # Dictionary to store documents centrally by their ID.
    
    # Method to update or add a document in the central repository.
    def update_document(self, doc_id, content):
        self.documents[doc_id] = content  # Update the document content.
        print(f"Document {doc_id} updated in Central Repository")  # Print confirmation message.

    # Method to synchronize documents from the central repository to all provided edge nodes.
    def sync_with_edge(self, edge_nodes):
        for doc_id, content in self.documents.items():  # Iterate through each document in the central repository.
            for node in edge_nodes:  # For each document, iterate through the list of edge nodes.
                node.update_document(doc_id, content)  # Update the document at each edge node with the central version.

# Example usage
central_repo = CentralRepository()  # Instantiate the central repository.
edge_node1 = EdgeNode("Edge Node 1")  # Create the first edge node.
edge_node2 = EdgeNode("Edge Node 2")  # Create the second edge node.

# Updating a document in the central repository.
central_repo.update_document("Doc1", "Confidential Content")

# Synchronizing the updated document with edge nodes to ensure data consistency across the system.
central_repo.sync_with_edge([edge_node1, edge_node2])
