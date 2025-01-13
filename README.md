# Cryptographic-Commitments-and-Field-Elements
This repo contains two Python examples demonstrating different cryptographic concepts. One involves a simple commitment scheme for age verification using SHA-256 hashing, and the other demonstrates elliptic curve cryptography with field elements using the ecdsa library.

##**1. Commitment Scheme for Age Verification (SHA-256)**
This code snippet demonstrates a simple cryptographic approach where a user can prove their age (e.g., if they are over 18) without revealing their exact age or date of birth. The process uses SHA-256 hashing to create a commitment to the user's birth date, and the verifier can check if the user meets the age criteria.

###**How It Works:**
1.	The user inputs their date of birth and a secret key.
2.	The system hashes this information to generate a cryptographic commitment.
3.	The system can then verify that the user’s age is above a certain threshold (e.g., 18) without revealing the exact date of birth.

###**Usage:**

•	The user inputs their birthdate and a secret key.
•	The system generates a cryptographic commitment to the user's age.
•	The verifier checks if the commitment matches the user's age and if the age is above the required threshold.

###**How to Run**
        Run the script in a Python environment or Jupyter Notebook.
        The output will indicate whether the age verification passed based on the user's birthdate.


##**2. Field Elements in Elliptic Curve Cryptography (ECDSA)**
This code snippet demonstrates how to work with field elements in elliptic curve cryptography using the ecdsa library. It creates a field element from an integer and prints the underlying representation. This approach is useful for more advanced cryptographic protocols such as Zero-Knowledge Proofs (ZKPs) and ECDSA signatures.

This code mimics the functionality of this [Rust code](https://www.linkedin.com/posts/nelly-njeri-ab5b4b280_i-just-took-my-first-step-toward-building-activity-7283494718557097984-E788?utm_source=share&utm_medium=member_desktop) which uses the Arkworks library for cryptographic field operations. Python does not have a direct equivalent of Arkworks' finite field operations, so you would typically handle these using libraries such as pycryptodome for random number generation or ecdsa for elliptic curve operations.

###**How It Works:**
•	This example uses the ecdsa library to create a finite field element, representing an element of a finite field.

•	The field element is printed, and its underlying representation is shown.
###**Requirements:**
To run the code, you'll need to install the ecdsa library:

###**How to Run**
        Run the script after installing the ecdsa library.
        The output will print the field element and its underlying representation.
