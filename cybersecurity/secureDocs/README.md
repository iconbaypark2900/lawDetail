# Integrated System Documentation

## Part 1: Blockchain Management (`sems.py`)

### Overview

This script simulates a simple blockchain system where each block contains data and is cryptographically linked to the previous block, ensuring data integrity and immutability.

### Functions

#### `create_block(content, previous_hash="")`
- **Arguments**:
  - `content (str)`: Content or data to be included in the block.
  - `previous_hash (str)`: Hash of the previous block in the chain.
- **Returns**:
  - `str`: Hash of the newly created block.
- **Description**:
  - This function concatenates the block's content with the previous block's hash, creates a block string, and generates a SHA-256 hash for it.

#### `add_to_blockchain(blockchain, new_data)`
- **Arguments**:
  - `blockchain (list)`: Blockchain, represented as a list of block hashes.
  - `new_data (str)`: Data to be stored in the new block.
- **Returns**:
  - `str`: Hash of the newly added block.
- **Description**:
  - Retrieves the hash of the last block (if any), creates a new block with the new data and appends it to the blockchain.

### Example Usage
```python
blockchain = []
add_to_blockchain(blockchain, "Energy usage data for 01/01/2024")
print("Blockchain:", blockchain)

# Smart Contract Ledger (`sems.sol`)

## Overview

This Solidity smart contract, `SmartCityLedger`, is designed to manage environmental data and citizen feedback within a smart city context. The contract aims to utilize blockchain technology for secure and immutable recording of relevant city data and public interactions.

## Contract Structures

### EnvironmentalData

#### Attributes:
- **timestamp** (`uint256`): Timestamp of the data entry, indicating when the data was recorded.
- **dataType** (`string`): Type of environmental data being stored (e.g., temperature, humidity).
- **dataValue** (`uint256`): The numeric value of the recorded environmental data.

### Feedback

#### Attributes:
- **citizen** (`address`): Ethereum address of the citizen submitting feedback, ensuring accountability.
- **message** (`string`): Content of the feedback provided by the citizen, capturing public sentiment or concerns.
- **timestamp** (`uint256`): Timestamp of when the feedback was submitted, providing a temporal context to the feedback.

## Functions

### `storeEnvironmentalData(dataType, dataValue)`
- **Description**: Allows any user to store data regarding the environment. This function is critical for collecting real-time, decentralized environmental data which can be used for various urban planning and public health assessments.
- **Usage**: Any user, such as city sensors or public apps, can call this function to contribute data.

### `submitFeedback(message)`
- **Description**: Enables citizens to submit feedback directly onto the blockchain, fostering a transparent and responsive civic engagement platform.
- **Usage**: Citizens can use this function to voice concerns, suggestions, or feedback about city services or events, enhancing community involvement.

## Modifiers

### `onlyCityOfficial`
- **Description**: Restricts certain administrative functions to the city official's Ethereum address.
- **Usage**: Applied to functions that should only be executable by city officials, such as modifying critical data or settings within the contract.

---

This `README.md` document thoroughly describes the `SmartCityLedger` contract's purpose, functionalities, and how it integrates within a smart city's ecosystem to leverage blockchain for data integrity and public engagement.

# Document Integrity Verification (`veriHash.py`)

## Overview

This Python script, `veriHash.py`, is designed to manage the integrity of documents through SHA-256 hashing. It provides functionalities for generating hashes from document contents and verifying the integrity of these documents by comparing hashes.

## Functions

### `generate_document_hash(document_contents)`

#### Arguments:
- **document_contents** (`str`): Content of the document to be hashed.

#### Returns:
- **str**: SHA-256 hash of the document, providing a unique identifier and ensuring the integrity of the document's content.

### `verify_document_integrity(original_hash, current_contents)`

#### Arguments:
- **original_hash** (`str`): The SHA-256 hash that was originally generated for the document, used as the benchmark for verification.
- **current_contents** (`str`): The current contents of the document that need to be verified against the original hash.

#### Returns:
- **tuple**: A boolean indicating whether the integrity of the document is maintained, along with a message stating the verification result.

## Example Usage

This example demonstrates how to use the functions within `veriHash.py` to ensure the integrity of document contents:

```python
# Generate the hash for the original document content
original_hash = generate_document_hash("This is the original document.")

# Verify the integrity of the document by comparing the original hash with the hash of the current contents
verification_result, message = verify_document_integrity(original_hash, "This is the original document.")

# Print the verification result
print(message)  # Expected Output: "Document integrity verified."
