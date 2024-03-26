from Crypto.PublicKey import RSA  # Imports the RSA module for asymmetric encryption.
from Crypto.Cipher import PKCS1_OAEP, AES  # Imports the PKCS1_OAEP and AES modules for encryption.
from Crypto.Random import get_random_bytes  # Imports the function to generate random bytes.

def hybrid_encrypt(data, public_key):
    """
    Encrypts data using a hybrid approach that combines RSA and AES encryption.
    
    Args:
    data (str): The plaintext data to encrypt.
    public_key (RSA obj): The RSA public key used to encrypt the AES key.
    
    Returns:
    tuple: Encrypted AES key, AES nonce, AES tag, and ciphertext.
    """
    # Generate a random AES key of 16 bytes for symmetric encryption.
    aes_key = get_random_bytes(16)
    
    # Encrypt the plaintext data with AES.
    aes_cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = aes_cipher.encrypt_and_digest(data.encode('utf-8'))
    
    # Encrypt the AES key with the RSA public key for secure key exchange.
    rsa_cipher = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)
    
    return encrypted_aes_key, aes_cipher.nonce, tag, ciphertext

def hybrid_decrypt(encrypted_aes_key, nonce, tag, ciphertext, private_key):
    """
    Decrypts data encrypted with the hybrid approach.
    
    Args:
    encrypted_aes_key (bytes): The encrypted AES key.
    nonce (bytes): The nonce used for AES encryption.
    tag (bytes): The tag used for verifying AES decryption.
    ciphertext (bytes): The encrypted data.
    private_key (RSA obj): The RSA private key used to decrypt the AES key.
    
    Returns:
    str: The decrypted plaintext data.
    """
    # Decrypt the AES key with the RSA private key.
    rsa_cipher = PKCS1_OAEP.new(private_key)
    aes_key = rsa_cipher.decrypt(encrypted_aes_key)
    
    # Decrypt the ciphertext with AES using the decrypted AES key.
    aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    data = aes_cipher.decrypt_and_verify(ciphertext, tag)
    
    return data.decode('utf-8')

# Example usage:
# Generate an RSA key pair for asymmetric encryption/decryption.
key_pair = RSA.generate(2048)
public_key = key_pair.publickey()  # The RSA public key.
private_key = key_pair  # The RSA private key.

# Simulate encrypting and decrypting data using the hybrid scheme.
original_data = "Confidential Smart Grid Data"
encrypted_aes_key, nonce, tag, ciphertext = hybrid_encrypt(original_data, public_key)
decrypted_data = hybrid_decrypt(encrypted_aes_key, nonce, tag, ciphertext, private_key)

print("Original Data:", original_data)
print("Decrypted Data:", decrypted_data)
