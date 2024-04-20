# Integrated Systems Documentation

## Overview

This documentation provides comprehensive details about the functionalities of the `failOver.py` and `recManage.py` scripts. These scripts are designed to handle data availability and consistency across a networked system of data centers and edge nodes.

## Part 1: Failover System (`failOver.py`)

### Overview

This section explains the `failOver.py` script, which implements a failover mechanism for data centers to ensure data availability if the primary data center fails.

### DataCenter Class

#### Attributes
- **name**: `string` - The name of the data center.
- **is_active**: `bool` - Indicates whether the data center is active.
- **documents**: `dict` - Stores documents by their ID.

#### Methods

##### Constructor: `__init__(self, name, is_active=True)`
1. Initializes a new Data Center with the specified name.
2. Sets the data center's active status, default is `True`.
3. Initializes an empty dictionary for storing documents.

##### `update_document(self, doc_id, content)`
1. Checks if the data center is active.
2. If active, updates the document with the specified ID and content.
3. Logs a success message indicating the document update.
4. If not active, logs a failure message.

### Failover System Function

#### `failover_system(primary, backups, doc_id, content)`
1. Checks if the primary data center is active.
2. If active, attempts to update the document in the primary center.
3. If the primary is not active, iterates through the list of backup centers.
4. Updates the document in the first active backup found.
5. Breaks the loop after the successful update.

#### Example Usage
```markdown
# Code Example
primary_dc = DataCenter("Primary DataCenter")
backup_dc1 = DataCenter("Backup DataCenter 1")
backup_dc2 = DataCenter("Backup DataCenter 2", is_active=False)  # Simulate a failure

failover_system(primary_dc, [backup_dc1, backup_dc2], "Doc2", "Important Legal Information")

# Record Management System Documentation

## Overview

This section of the documentation covers the `recManage.py` script, which is designed to manage document synchronization between a central repository and multiple edge nodes across a network. This ensures data consistency throughout the system.

## Classes and Functionalities

### EdgeNode Class

#### Attributes
- **name**: `string` - The name of the edge node.
- **documents**: `dict` - A dictionary that stores documents locally at the edge node.

#### Methods

##### Constructor: `__init__(self, name)`
- **Purpose**: Initializes an EdgeNode with the specified name.
- **Functionality**: Sets up a dictionary to store document information, facilitating local document management at the node.

##### `update_document(self, doc_id, content)`
- **Purpose**: Adds new or updates existing documents at the edge node.
- **Functionality**: Modifies the local document storage with updated content and confirms the update, ensuring the document's current state is preserved at the node level.

### CentralRepository Class

#### Attributes
- **documents**: `dict` - Centrally stores documents by their ID, serving as the main repository for all document data.

#### Methods

##### Constructor: `__init__(self)`
- **Purpose**: Initializes the CentralRepository.
- **Functionality**: Sets up a central storage for documents, which acts as the primary source of document data within the network.

##### `update_document(self, doc_id, content)`
- **Purpose**: Updates or adds documents within the central repository.
- **Functionality**: Ensures that the central repository has the most current version of each document, making it ready for synchronization across the network.

##### `sync_with_edge(self, edge_nodes)`
- **Purpose**: Synchronizes all documents stored in the central repository with each connected edge node.
- **Functionality**: Iterates through each document in the central repository and updates every edge node to maintain consistency across the network. This is crucial for operations where multiple nodes must have up-to-date document information.

## Example Usage

To demonstrate the functionality of this script, consider the following setup:

```markdown
# Setup
central_repo = CentralRepository()  # Initialize the central repository.
edge_node1 = EdgeNode("Edge Node 1")  # Create the first edge node.
edge_node2 = EdgeNode("Edge Node 2")  # Create the second edge node.

# Update and Synchronization
central_repo.update_document("Doc1", "Updated Content")  # Update a document in the central repository.
central_repo.sync_with_edge([edge_node1, edge_node2])  # Synchronize the updated document with edge nodes.
