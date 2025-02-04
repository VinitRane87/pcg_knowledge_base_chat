from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt plaintext using 3DES
def triple_des_encrypt(key, plaintext):
    """
    Encrypts a plaintext string using 3DES encryption.

    :param key: A 16 or 24-byte key
    :param plaintext: The plaintext string to encrypt
    :return: The ciphertext and initialization vector (IV)
    """
    # Create a cipher object using the key and a random IV
    cipher = DES3.new(key, DES3.MODE_CBC)
    iv = cipher.iv

    # Pad the plaintext to ensure it's a multiple of the block size
    padded_plaintext = pad(plaintext.encode('utf-8'), DES3.block_size)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext, iv

# Function to decrypt ciphertext using 3DES
def triple_des_decrypt(key, ciphertext, iv):
    """
    Decrypts a ciphertext string using 3DES encryption.

    :param key: A 16 or 24-byte key
    :param ciphertext: The encrypted ciphertext
    :param iv: The initialization vector (IV) used during encryption
    :return: The decrypted plaintext string
    """
    # Create a cipher object using the key and the provided IV
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)

    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)

    # Unpad the plaintext
    plaintext = unpad(padded_plaintext, DES3.block_size).decode('utf-8')
    return plaintext

# Example usage
if __name__ == "__main__":
    # Generate a valid 16 or 24-byte key for 3DES
    while True:
        key = get_random_bytes(24)  # Generate a random 24-byte key
        if DES3.key_size == len(key):
            break

    # Input plaintext
    plaintext = "3DES Encryption!"
    print(f"Original Text: {plaintext}")

    # Encrypt the plaintext
    ciphertext, iv = triple_des_encrypt(key, plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}")

    # Decrypt the ciphertext
    decrypted_text = triple_des_decrypt(key, ciphertext, iv)
    print(f"Decrypted Text: {decrypted_text}")