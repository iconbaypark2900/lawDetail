import ssl  # Imports the SSL module to handle encryption for network connections.
import socket  # Imports the socket module for network connections.

def secure_transmission(host='localhost', port=443):
    """
    Establishes a secure SSL/TLS connection to the specified host and port, sends a greeting message, and receives a response.
    
    Args:
    host (str): The hostname or IP address of the server. Defaults to 'localhost'.
    port (int): The port number of the server. Defaults to 443, the standard port for HTTPS.
    """
    # Create an SSL context with default configurations for secure connections.
    # This context is set up for client-side verification with strict certificate verification.
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    
    # To establish a secure connection, the client's certificate and private key can be loaded here.
    # This is necessary for servers that require client authentication.
    # Example: context.load_cert_chain(certfile="path/to/clientcert.pem", keyfile="path/to/clientkey.pem")
    
    # Create a plain socket connection to the server.
    with socket.create_connection((host, port)) as sock:
        # Upgrade the plain socket connection to a secure socket using the SSL context.
        with context.wrap_socket(sock, server_hostname=host) as secure_sock:
            # Once the SSL connection is established, print the server's certificate details.
            print(f"SSL established. Peer: {secure_sock.getpeercert()}")
            
            # Send a greeting message to the server over the secure connection.
            secure_sock.sendall(b"Hello, secure world!")
            # Wait for and receive the response from the server.
            response = secure_sock.recv(1024)
            # Print the received response after decoding it from bytes to a string.
            print(f"Received: {response.decode('utf-8')}")

# Note: For this code to function correctly in a real scenario, a server with a valid SSL/TLS certificate must be running on the specified host and port.
# The server must also be configured to accept secure connections and potentially verify client certificates if client authentication is required.

