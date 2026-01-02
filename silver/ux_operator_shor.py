from qiskit.quantum_info import Operator
import numpy as np

def Ux(x, N):
    # Number of qubits
    k = 1
    while 2**k < N:
        k += 1

    # Initialize matrix
    u = np.zeros((2**k, 2**k), dtype=int)

    # Fill in modular multiplication
    for i in range(N):
        # Convert i to binary, reverse bits to match Qiskit LSB-first
        i_bits = [int(b) for b in format(i, f'0{k}b')]
        i_le = int("".join(str(b) for b in i_bits[::-1]), 2)

        # Compute x*i mod N, also reverse bits
        xi = (x*i) % N
        xi_bits = [int(b) for b in format(xi, f'0{k}b')]
        xi_le = int("".join(str(b) for b in xi_bits[::-1]), 2)

        u[xi_le][i_le] = 1

    # Identity for remaining states
    for i in range(N, 2**k):
        u[i][i] = 1

    return Operator(u)
