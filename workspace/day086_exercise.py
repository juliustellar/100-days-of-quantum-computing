from random import Random

rng = Random(7)
alice_bits = [rng.randrange(2) for _ in range(12)]
alice_basis = [rng.randrange(2) for _ in range(12)]
bob_basis = [rng.randrange(2) for _ in range(12)]
sifted = [bit for bit, a, b in zip(
    alice_bits, alice_basis, bob_basis) if a == b]
print(sifted)
