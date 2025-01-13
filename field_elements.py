from ecdsa import Fq, numbertheory

# Creating a field element from a number (equivalent to `Fq::from(42u64)` in Rust)
field_element = Fq(42)

# Printing the field element
print(f"field element: {field_element}")

# Converting the field element to its underlying representation (as a big integer)
repr = field_element
print(f"underlying representation: {repr}")
