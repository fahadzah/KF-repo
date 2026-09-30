"""Deliberately weak/deprecated crypto usage for AgileSec GitHub sensor test coverage."""
import hashlib
import ssl
from Crypto.Cipher import DES

def hash_password(pw: str) -> str:
    # deprecated: MD5 for password hashing
    return hashlib.md5(pw.encode()).hexdigest()

def legacy_hash(data: bytes) -> str:
    # deprecated: SHA-1
    return hashlib.sha1(data).hexdigest()

def make_legacy_ssl_context():
    # deprecated: TLS 1.0
    return ssl.SSLContext(ssl.PROTOCOL_TLSv1)

def weak_encrypt(key: bytes, data: bytes) -> bytes:
    # deprecated: DES (56-bit, broken)
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

# Hardcoded private key embedded directly in source (not a separate file) -
# deliberate test case for source-level secret detection.
HARDCODED_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBALbAUaQgaKZQWS9f
78XPlAOf00zLBVfg+vlwu6/br4/iEZNQOjXomr9b7PipV5UfZjDKi948jwtXG15F
qaOBKbD+TCDVff6jwR/CubL1/i6tvyGdZKEmRgeEtbjNi0Te26h7vlnYJVf2r8+K
F46nYogpi6G5wCApMhzNhGV4Hz9jAgMBAAECgYBK1S2ZG3w+viAG+i3gvkNJyKRp
iajCd2nNwo/YTwjwzg2MWQm9EWZsfWPn3s/yTE04JXhopDue1ShrzfLM9RLwqcIL
Vc/6RBb/JD2KDDBpGDzmK+A/1DUlryccI89Njv7ctQZpeEsRVRe+HrRiJum3BM+7
4deWGutfMF8W5THboQJBAN0TSUYRgO7Ym4c+8MX9ltEEZZoHvsxzZ5i7dU0niFac
IDr1j+zAxkHE/JgPUsZk9eIAi/k4G6A85vmWarctpl0CQQDTnyHkj2eTFqgR182o
D6c7zKVDhV9QHxMd9OPjfY5grLRJwoHQVXs69HxEFeLdGYXHHctxqhfRolmLwG0c
DqC/AkBKNYIgKhn8kutKL9+EpoYsrWwpkzYBzS9WPn62onGKmSfcgreIQoGKbERa
CrK/c/5xmbtisencFPV3jH1P9dvlAkEAwn6p/s/SKLyVAbkumbyxPeOrLHCDFjdJ
MaomXKnD1pREKtpqxtgZpyiWoVjgJcdUTZnTpobm11P4KtpTLYtALwJBAJbdfPCP
Iu6ZV/D9IK7icXgrDzkaKI96JtsLT4NfaBkKguK1Kk7tleEiLv7NP3++BFv4kR5d
xN2CyYnvEWpZUz0=
-----END PRIVATE KEY-----"""
