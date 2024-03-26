# Define a class to represent a data center.
class DataCenter:
    # Initialize a new Data Center with a name and its active status. By default, a data center is active.
    def __init__(self, name, is_active=True):
        self.name = name  # Name of the data center.
        self.is_active = is_active  # Boolean indicating if the data center is currently active.
        self.documents = {}  # Dictionary to store documents by their ID.

    # Method to update or add a document in this data center if it's active.
    def update_document(self, doc_id, content):
        if self.is_active:
            self.documents[doc_id] = content  # Update the document content.
            print(f"Document {doc_id} updated in {self.name}")
        else:
            print(f"Failed to update in {self.name}: DataCenter not active")

# A function that attempts to update a document in the primary data center, but uses backup centers if the primary is inactive.
def failover_system(primary, backups, doc_id, content):
    if primary.is_active:
        primary.update_document(doc_id, content)  # Try updating in the primary center first.
    else:
        for backup in backups:  # If primary is down, iterate through the list of backups.
            if backup.is_active:  # Check if the backup is active.
                backup.update_document(doc_id, content)  # Update the document in the first active backup found.
                break  # Exit loop after successful update.

# Example usage
primary_dc = DataCenter("Primary DataCenter")  # Creating the primary data center.
backup_dc1 = DataCenter("Backup DataCenter 1")  # Creating the first backup data center.
backup_dc2 = DataCenter("Backup DataCenter 2", is_active=False)  # Creating a second backup, marked as inactive to simulate a failure.

# Attempting to update a document, utilizing the failover system in case the primary data center is down.
failover_system(primary_dc, [backup_dc1, backup_dc2], "Doc2", "Important Legal Information")

