# KF-repo

Throwaway test repository for the CAD-POC-KeyFactor project's AgileSec
GitHub code-repo sensor testing. Not a real project — contains
deliberately weak/deprecated crypto material and hardcoded secrets for
detection-accuracy testing only.

## Contents
- `certs/` — planted X.509 certs: `weak-rsa1024-sha1` (deliberately weak),
  `good-rsa2048` (baseline), `pqc-mldsa65` (post-quantum ML-DSA-65)
- `src/weak_crypto.py` / `src/weak_crypto.go` — deprecated crypto API usage
  (MD5, SHA-1, DES, TLSv1) plus a hardcoded private key embedded directly
  in source
