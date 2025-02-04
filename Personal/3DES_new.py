from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def triple_des_encrypt(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_CBC)  # Use 3DES, not DES
    iv = cipher.iv  # Get the initialization vector
    padded_text = pad(plaintext.encode('utf-8'), DES3.block_size)  # Pad the plaintext
    ciphertext = cipher.encrypt(padded_text)  # Encrypt the padded plaintext
    return ciphertext, iv

def triple_des_decrypt(key, ciphertext, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)  # Use 3DES, not DES
    decrypted_padded_text = cipher.decrypt(ciphertext)  # Decrypt the ciphertext
    decrypted_text = unpad(decrypted_padded_text, DES3.block_size)  # Unpad the decrypted text
    return decrypted_text.decode()

if __name__ == "__main__":
    # Generate a 24-byte key for 3DES encryption
    key = DES3.adjust_key_parity(get_random_bytes(24))  # Ensures the key meets 3DES parity requirements
    plaintext = "Hello CSUDH, Using 3DES Encryption!"
    print(f"Original Text: {plaintext}")

    # Encrypt the plaintext
    ciphertext, iv = triple_des_encrypt(key, plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}")

    # Decrypt the ciphertext
    decrypted_text = triple_des_decrypt(key, ciphertext, iv)
    print(f"Decrypted Text: {decrypted_text}")