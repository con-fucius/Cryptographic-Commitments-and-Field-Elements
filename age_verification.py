from hashlib import sha256

def hash_data(data):
    """Hashes data using SHA-256."""
    return sha256(data.encode()).hexdigest()

def generate_commitment(date_of_birth, secret_key):
    """Generates a commitment to the date of birth."""
    data = f"{date_of_birth}{secret_key}"
    return hash_data(data)

def verify_age(commitment, secret_key, date_of_birth, min_age):
    """Verifies the age without revealing the actual date of birth."""
    from datetime import datetime
    current_year = datetime.now().year
    birth_year = int(date_of_birth.split("-")[0])
    age = current_year - birth_year

    # Recompute commitment
    recomputed_commitment = generate_commitment(date_of_birth, secret_key)

    # Verify commitment and age
    return commitment == recomputed_commitment and age >= min_age

# Example Usage
date_of_birth = "2000-01-01"
secret_key = "random_secret"
min_age = 18

# User generates commitment
commitment = generate_commitment(date_of_birth, secret_key)

# Verifier checks the commitment and age
is_valid = verify_age(commitment, secret_key, date_of_birth, min_age)

print("Age verification passed:", is_valid)
