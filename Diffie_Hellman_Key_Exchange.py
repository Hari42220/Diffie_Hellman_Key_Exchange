# key exchange using Diffie-Hellman key exchange

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh

# Generate the parameters for the key exchange.
parameters = dh.generate_parameters(generator=2, key_size=512, backend=default_backend())

# Generate a private key for "Diffie".
diffie_private_key = parameters.generate_private_key()

# Generate the public key for "Diffie".
diffie_public_key = diffie_private_key.public_key()

# Generate a private key for "Hellman".
hellman_private_key = parameters.generate_private_key()

# Generate the public key for "Hellman".
hellman_public_key = hellman_private_key.public_key()

# "Diffie" computes the shared secret.
diffie_shared_secret = diffie_private_key.exchange(hellman_public_key)

# "Hellman" computes the shared secret.
hellman_shared_secret = hellman_private_key.exchange(diffie_public_key)

# Compare the shared secrets to ensure they match.
if diffie_shared_secret == hellman_shared_secret:
    print("Key exchange successful.")
else:
    print("Key exchange failed.")