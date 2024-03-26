# Import the sha256 function from the hashlib library to generate hash values.
from hashlib import sha256

def create_block(content, previous_hash=""):
    """
    Creates a new block in the blockchain.

    Args:
    content (str): The content or data to be included in the block.
    previous_hash (str): The hash of the previous block in the chain. Defaults to an empty string.

    Returns:
    str: The hash of the newly created block.
    """
    # Concatenate the content with the previous block's hash to form the block string.
    block_string = f"{content}{previous_hash}"
    # Generate a SHA-256 hash of the block string. The hash serves as the block's unique identifier.
    block_hash = sha256(block_string.encode()).hexdigest()
    return block_hash

def add_to_blockchain(blockchain, new_data):
    """
    Adds a new block to the blockchain.

    Args:
    blockchain (list): The blockchain represented as a list of block hashes.
    new_data (str): The data to be stored in the new block.

    Returns:
    str: The hash of the newly added block.
    """
    # Get the hash of the last block in the blockchain if it exists, or use an empty string.
    previous_hash = blockchain[-1] if blockchain else ""
    # Create a new block with the provided data and the hash of the previous block.
    new_block_hash = create_block(new_data, previous_hash)
    # Append the hash of the new block to the blockchain.
    blockchain.append(new_block_hash)
    return new_block_hash

# Example usage of the blockchain
# Initialize an empty list to represent the blockchain.
blockchain = []
# Add a new block containing energy usage data for 01/01/2024.
add_to_blockchain(blockchain, "Energy usage data for 01/01/2024")
# Add another block with data for the next day.
add_to_blockchain(blockchain, "Energy usage data for 01/02/2024")

# Print the current state of the blockchain, displaying the hashes of all blocks.
print("Blockchain:", blockchain)

