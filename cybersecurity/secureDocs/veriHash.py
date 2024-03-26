import hashlib  # Imports the hashlib library for accessing SHA-256 hashing functionality.

def generate_document_hash(document_contents):
    """
    Generates a SHA-256 hash for the given document contents.
    
    Args:
    document_contents (str): The content of the document to hash.
    
    Returns:
    str: A hexadecimal string representing the SHA-256 hash of the document.
    """
    sha256_hash = hashlib.sha256()  # Creates a new SHA-256 hash object.
    sha256_hash.update(document_contents.encode('utf-8'))  # Encodes the document contents in UTF-8 and updates the hash object with it.
    return sha256_hash.hexdigest()  # Returns the hexadecimal digest of the hash.

def verify_document_integrity(original_hash, current_contents):
    """
    Verifies the integrity of a document by comparing its current hash with the original hash.
    
    Args:
    original_hash (str): The original hash of the document for comparison.
    current_contents (str): The current contents of the document to verify.
    
    Returns:
    tuple: A boolean indicating if the document's integrity is verified and a message stating the result.
    """
    current_hash = generate_document_hash(current_contents)  # Generates the hash of the current document contents.
    if current_hash == original_hash:  # Compares the current hash to the original hash.
        return True, "Document integrity verified."  # Returns true if the hashes match, indicating no tampering.
    else:
        return False, "Document integrity compromised."  # Returns false if the hashes don't match, indicating potential tampering.

# Example usage of the functions above.
original_document = "This is the original document."  # Example original document text.
original_hash = generate_document_hash(original_document)  # Generates the hash of the original document.

# Simulating the process of verifying the integrity of the document.
# Here, the current document contents are the same as the original.
current_document = "This is the original document."
verification_result, message = verify_document_integrity(original_hash, current_document)  # Verifies the document's integrity.
print(message)  # Prints the result of the integrity verification.
