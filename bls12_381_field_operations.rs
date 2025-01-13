src>bls12_381_ field _operations.rs >
use ark_ff: : (Field, PrimeField);
use ark_test_ curves::bls12_381: :Fq;
use ark_std: : (One, UniformRand)

fn main() {
// Creating a field element from a number
let field_ element = Fq:: from(42u64);
let S string from: ('hello')
// Printing the field element
println! ("field element: {:?}"
field_element)
// Converting the field element to its underlying representation
let repr=field_element.into_bigint()
println! ("underlying representation: (:?)", repr);
