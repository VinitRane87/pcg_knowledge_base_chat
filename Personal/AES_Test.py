from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt plaintext
def aes_encrypt(key, plaintext):
    """
    Encrypts a plaintext string using AES encryption.

    :param key: A 16, 24, or 32-byte key
    :param plaintext: The plaintext string to encrypt
    :return: The ciphertext and initialization vector (IV)
    """
    # Create a cipher object using the key and a random IV
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    # Pad the plaintext to ensure it's a multiple of 16 bytes
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext, iv

# Function to decrypt ciphertext
def aes_decrypt(key, ciphertext, iv):
    """
    Decrypts a ciphertext string using AES encryption.

    :param key: A 16, 24, or 32-byte key
    :param ciphertext: The encrypted ciphertext
    :param iv: The initialization vector (IV) used during encryption
    :return: The decrypted plaintext string
    """
    # Create a cipher object using the key and the provided IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)

    # Unpad the plaintext
    plaintext = unpad(padded_plaintext, AES.block_size).decode('utf-8')
    return plaintext

# Example usage
if __name__ == "__main__":
    # Generate a random 16-byte key
    key = get_random_bytes(16)  # Key must be 16, 24, or 32 bytes long

    # Input plaintext
    plaintext = "Hello, CSUDH AES encryption!"
    print(f"Original Text: {plaintext}")

    # Encrypt the plaintext
    ciphertext, iv = aes_encrypt(key, plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}")

    # Decrypt the ciphertext
    decrypted_text = aes_decrypt(key, ciphertext, iv)
    print(f"Decrypted Text: {decrypted_text}")