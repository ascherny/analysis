from Crypto.Cipher import AES
import base64

cipher_b64 = "nBqvn7LpG+iRRABKO/uHcZ/mFuCTCGQQXoozH+34uWm6yspl6ZaTEcnwHMC4p+/Q"
key = b"super_secret_key"
iv = bytes(16)

ciphertext = base64.b64decode(cipher_b64.replace(" ", ""))
plaintext = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)

print(plaintext.rstrip(b"\t").decode())

#H7CTF{3332a9620a6d9be910600b94fe5b678e}


# 48 = 16 + 16 + 16 → часто это (IV16) || (CT 16) || (TAG16) — типичный вид для AES‑GCM (IV 16 возможен) или просто 3 блока шифртекста.
# Также 48 = 12 + 20 + 16 → если IV = 12 (частая длина для GCM), CT может быть 20 байт.