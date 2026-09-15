import base64
import hashlib
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# ----------------------------------- For the AES-256 algorithm ----------------------------------- #

SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32              
PBKDF2_ITERATIONS = 600_000

# Key:
def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        PBKDF2_ITERATIONS,
        dklen=KEY_SIZE
    )


# Encryption:
def encrypt(plaintext: str, password: str) -> str:
    salt = os.urandom(SALT_SIZE)
    key = derive_key(password, salt)
    nonce = os.urandom(NONCE_SIZE)
    aes = AESGCM(key)
    ciphertext = aes.encrypt(
        nonce,
        plaintext.encode("utf-8"),
        None
    )
    combined = salt + nonce + ciphertext
    return base64.urlsafe_b64encode(combined).decode("ascii")


# Decryption:
def decrypt(encoded: str, password: str) -> str:
    try:
        data = base64.urlsafe_b64decode(encoded)
        salt = data[:SALT_SIZE]
        nonce = data[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
        ciphertext = data[SALT_SIZE + NONCE_SIZE:]
        key = derive_key(password, salt)
        aes = AESGCM(key)
        plaintext = aes.decrypt(
            nonce,
            ciphertext,
            None
        )
        return plaintext.decode("utf-8")
    except Exception:
        raise ValueError(
            "Decryption failed: incorrect key or corrupted ciphertext."
        )